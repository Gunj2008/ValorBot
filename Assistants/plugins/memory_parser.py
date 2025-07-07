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
                "You are a memory extraction assistant. "
                "Given a user message, extract only the values they mention for name, city, or interests. "
                "Return your response as a JSON object ONLY — no commentary, no extra text. "
                "Example:\n"
                "Input: My name is Priya and I live in Delhi.\n"
                "Output: {\"name\": \"Priya\", \"city\": \"Delhi\"}"
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