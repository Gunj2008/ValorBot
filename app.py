import gradio as gr
from Assistants.chat import ask_valor
from Assistants.plugins.weather import get_weather
from Assistants.plugins.todo import add_task, show_tasks
from Assistants.plugins.memory import get_profile
from Assistants.plugins.memory_parser import extract_memory_updates
from Assistants.plugins.email_summary import fetch_recent_emails, summarize_emails
from Assistants.plugins.voice_io import speak
import speech_recognition as sr

def valor_response(user_input):

    if not user_input.strip():
        return "Please type or say something."
    
    user_input = user_input.strip().lower()

    if user_input in ["quit", "exit"]:
        return "Goodbye!"
    
    elif user_input.startswith("weather in "):
        city = user_input.replace("weather in ", "").strip()
        return get_weather(city)
    
    elif user_input.startswith("add task "):
        task = user_input.replace("add task ", "").strip()
        return add_task(task)
    
    elif user_input == "show tasks":
        return show_tasks()
    
    elif "summarise my inbox" in user_input:
        emails = fetch_recent_emails(limit=5)
        return summarize_emails(emails)
    
    elif any (phrase in user_input for phrase in ["what do you remember about me", "show my memory", "my profile"]):
        return get_profile()
    
    # elif any(p in user_input for p in ["remember", "my name", "i live", "i like"]):
    #     return extract_memory_updates(user_input)
    
    else:
        response = extract_memory_updates(user_input)
        if response:
            return response
        else:
            return ask_valor(user_input)
    
    
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    
    try:
        return recognizer.recognize_google(audio)
        
    except sr.UnknownValueError:
        return "Sorry I didn't catch that.", ""
    
    except sr.RequestError as e:
        return f"Speech service error: {e}", ""
    

def handle_voice(audio_path):
    transcript = transcribe_audio(audio_path)
    response = valor_response(transcript)
    speak(response)
    return transcript, response


def handle_text(input_text):
    response = valor_response(input_text)
    speak(response)
    return input_text, response


with gr.Blocks() as iface:
    gr.Markdown(
        """
        # ValorBot
        **Your Personal AI Assistant**  
        Talk or type — I'll help with weather, tasks, memory, and email!
        ---
        """
    )

    with gr.Row():

        with gr.Column(scale = 1):
            mic_input = gr.Audio(sources = ["microphone"], type = "filepath", label = "Speaak to ValorBot")
            mic_transcript = gr.Textbox(label = "Transcribed Text")

        with gr.Column(scale = 2):
            user_input = gr.Textbox(label = "Type here ...")
            submit_btn = gr.Button("Send")
            bot_reply = gr.Textbox(label = "ValorBot says ...", lines = 6)
    
    mic_input.change(fn = handle_voice, inputs = mic_input, outputs = [mic_transcript, bot_reply])
    submit_btn.click(fn = handle_text, inputs = user_input, outputs = [user_input, bot_reply])


if __name__ == "__main__":
    iface.launch()