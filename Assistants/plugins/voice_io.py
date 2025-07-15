import pyttsx3
from gtts import gTTS
from playsound import playsound
import threading
import speech_recognition as sr
import queue
import time
import uuid
import os

engine = pyttsx3.init()
engine.setProperty('rate', 175)

speech_queue = queue.Queue()

def speech_worker():
    while True:

        try:
            text = speech_queue.get()

            if text is None:
                break

            engine.say(text)
            engine.runAndWait()
            speech_queue.task_done()

        except Exception as e:
            print(f"Speach thread error: {e}")
            time.sleep(0.5)

if not hasattr(engine, "_speech_thread_started"):
    threading.Thread(target = speech_worker, daemon = True).start()
    engine._speech_thread_started = True

def speak(text):
    print(f"ValorBot: {text}")
    if not text.strip():
        return
    
    try:
        filename = f"temp_{uuid.uuid4().hex}.mp3"
        gTTS(text).save(filename)
        playsound(filename)
        os.remove(filename)

    except Exception as e:
        print({f"Speech error: {e}"})
        

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