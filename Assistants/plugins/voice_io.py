import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print(f"ValorBot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...(say something)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You : {query}")
        return query
    
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch it.")

    except sr.RequestError:
        speak("Sorry, there's a proble with the speech service.")
    return ""