from Assistants.chat import ask_valor
from Assistants.plugins.weather import get_weather
from Assistants.plugins.todo import add_task, show_tasks
from Assistants.plugins.memory_parser import extract_memory_updates
from Assistants.plugins.memory import get_profile
from Assistants.plugins.memory import load_profile
from Assistants.plugins.voice_io import listen, speak

use_voice = input("Do you want to use voice mode ? (y/n): ").strip().lower() == 'y'

profile = load_profile()
if profile['name']:
    print(f"Welcome back, {profile['name']}!")
else:
    print("Welcome to ValorBot! Type 'help' to see commands")

while True:
    user_input = listen() if use_voice else input("\n> ").strip().lower()

    if not user_input:
        continue

    if user_input in ["quit", "exit"]:
        speak("Goodbye!")
        break

    elif user_input.startswith("weather in "):
        city = user_input.replace("weather in ", "").strip()
        speak(get_weather(city))

    elif user_input.startswith("add task "):
        task = user_input.replace("add task ", "").strip()
        speak(add_task(task))

    elif user_input == "show tasks":
        speak(show_tasks())

    elif user_input == 'help':
        speak("""
  Commands:
  weather in [city]
  add task [task]
  show tasks
  [any question]
  exit / quit          
""")
        
    elif user_input.lower() in ["what do you remember about me", "show my memory", "my profile"]:
        speak(get_profile())
        
    else:
        response = extract_memory_updates(user_input)
        if "updated your profile" in response.lower():
            speak(response)
        else:
            speak(ask_valor(user_input))