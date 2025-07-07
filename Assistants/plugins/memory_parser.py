from Assistants.plugins.memory import update_profile
from config.settings import COHERE_API_KEY
import cohere
import json

co = cohere.Client(COHERE_API_KEY)

def extract_memory_updates(user_input):

    try:
        response = co.chat(
            model = 'command-r',
            message = user_input,
            temperature = 0.3,
            chat_history = [],
            preamble = (
                "You are a smart memory extraction assistant for a personal AI. "
                "When a user says anything about themselves, extract only what they tell you "
                "about their name, city (where they live), and interests (things they like). "
                "Always return a JSON object with only the fields they mentioned. "
                "Valid fields are: name (string), city (string), interests (list of strings). "
                "If the user doesn't say something, leave it out. "
                "Only return a valid JSON object — no explanations or extra text.\n\n"
                "Example output:\n"
                "{ \"name\": \"Aisha\", \"city\": \"Bangalore\", \"interests\": [\"books\", \"anime\"] }"
            )
        )

        raw_output = response.text
        clean_output = raw_output.encode('utf-8').decode('utf-8-sig').strip()

        parsed = json.loads(clean_output)

        for key, value in parsed.items():
            update_profile(key, value)

        return f"Got it! I've updated your profile with: {', '.join(parsed.keys())}"
    
    except Exception as e:
        return f"Couldn't understand what to remember. ({str(e)})"