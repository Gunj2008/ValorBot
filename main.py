from Assistants.chat import ask_valor
from Assistants.plugins.weather import get_weather
from Assistants.plugins.todo import add_task, show_tasks
from Assistants.plugins.memory_parser import extract_memory_updates
from Assistants.plugins.memory import get_profile
from Assistants.plugins.memory import load_profile

profile = load_profile()
if profile['name']:
    print(f"Welcome back, {profile['name']}!")
else:
    print("Welcome to ValorBot! Type 'help' to see commands")

while True:
    user_input = input("\n> ").strip().lower()

    if user_input in ["quit", "exit"]:
        print("Goodbye!")
        break

    elif user_input.startswith("weather in "):
        city = user_input.replace("weather in ", "").strip()
        print(get_weather(city))

    elif user_input.startswith("add task "):
        task = user_input.replace("add task ", "").strip()
        print(add_task(task))

    elif user_input == "show tasks":
        print(show_tasks())

    elif user_input == 'help':
        print("""
  Commands:
  weather in [city]
  add task [task]
  show tasks
  [any question]
  exit / quit          
""")
        
    elif user_input.lower() in ["what do you remember about me", "show my memory", "my profile"]:
        print(get_profile())
        
    else:
        response = extract_memory_updates(user_input)
        if "update your profile" in response.lower():
            print(response)
        else:
            print(ask_valor(user_input))