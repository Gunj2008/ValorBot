import gradio as gr
from Assistants.chat import ask_valor
from Assistants.plugins.weather import get_weather
from Assistants.plugins.todo import add_task, show_tasks
from Assistants.plugins.memory import get_profile
from Assistants.plugins.memory_parser import extract_memory_updates
from Assistants.plugins.email_summary import fetch_recent_emails, summarize_emails

def valor_ui(user_input):
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
    
    else:
        return ask_valor(user_input)
        # response = extract_memory_updates(user_input)
        # if response:
        #     return response
        # else:
        #     return ask_valor(user_input)
    
iface = gr.Interface(
    fn = valor_ui,
    inputs = gr.Textbox(label = "User Input", placeholder = "Type something..."),
    outputs = "text",
    title = "ValorBot",
    description = "Your perssonal AI assistant with memory, weather, to-do, email & more!",
    theme = "soft",
    allow_flagging = "never"
)

if __name__ == "__main__":
    iface.launch()