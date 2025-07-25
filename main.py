import os
from Assistants.chat import ask_valor
from Assistants.plugins.weather import get_weather
from Assistants.plugins.todo import add_task, show_tasks
from Assistants.plugins.memory_parser import extract_memory_updates
from Assistants.plugins.memory import get_profile
from Assistants.plugins.memory import load_profile
from Assistants.plugins.voice_io import listen, speak
from Assistants.plugins.email_summary import fetch_recent_emails, summarize_emails
from Assistants.plugins.doc_summary import extract_text_from_pdf, extract_text_from_doc, summarise_text
from Assistants.plugins.conversation import handle_multi_turn, clear_chat_memory

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
        if use_voice == 'y':
            speak("Goodbye!")
            break
        else:
            print("Goodbye!")
            break

    elif user_input.startswith("weather in "):
        city = user_input.replace("weather in ", "").strip()

        if use_voice == 'y':
            speak(get_weather(city))
        else:
            print(get_weather(city))

    elif user_input.startswith("add task "):
        task = user_input.replace("add task ", "").strip()

        if use_voice == 'y':
            speak(add_task(task))
        else:
            print(add_task(task))

    elif user_input == "show tasks":
        if use_voice == 'y':
            speak(show_tasks())
        else:
            print(show_tasks())

    elif user_input == 'help':
        if use_voice == 'y':
            speak("""
    Commands:
    weather in [city]
    add task [task]
    show tasks
    [any question]
    exit / quit          
    """)
        else:
            print("""
        Commands:
        weather in [city]
        add task [task]
        show tasks
        summarize file [path_to_pdf_or_docx]
        summarise my inbox
        show my memory / my profile
        exit / quit            
    """)
        
    elif user_input.lower() in ["what do you remember about me", "show my memory", "my profile"]:
        if use_voice == 'y':
            speak(get_profile())
        else:
            print(get_profile())

    elif "summarise my inbox" in user_input:
        emails = fetch_recent_emails(limit=5)
        summary = summarize_emails(emails)
        print("Email Summary: \n", summary)

    elif user_input.startswith("summarise file "):
        file_path = user_input.replace("summarise file ", "").strip()

        if not os.path.exists(file_path):
            speak("Sorry, I couldn't find that file.")
            continue

        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = extract_text_from_doc(file_path)
        else:
            speak("Unsupported file format. Please provide a PDF or DOCX file.")
            continue

        summary = summarise_text(text)
        if use_voice == 'y':
            speak("Summary : ", summary)
        else:
            print("Summary : ", summary)
            

        
    else:
        response = extract_memory_updates(user_input)

        if response:
            speak(response) if use_voice else print(response)
        elif user_input == "reset memory":
            clear_chat_memory()
            speak("Memory cleared.") if use_voice else print("Memory cleared.")
        else:
            reply = handle_multi_turn(user_input)
            speak(reply) if use_voice else print(reply)