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
            preamble=(
                "You are a memory extraction assistant. "
                "Extract ONLY if the user shares their name, city, or interests. "
                "Return a JSON object using any of: name (string), city (string), interests (list of strings). "
                "If nothing relevant is shared, respond with null (no quotes).\n\n"
                "Example:\n"
                "Input: My name is Priya and I live in Delhi.\n"
                "Output: {\"name\": \"Priya\", \"city\": \"Delhi\"}\n\n"
                "If irrelevant, output null only."
            )
        )

        raw_output = response.text.strip()
        
        if raw_output.lower() == "null":
            return None
        
        if not raw_output.startswith("{") and raw_output.lower() != "null":
            return None

        parsed = json.loads(raw_output)

        fake_values = {"ai", "chatgpt", "assistant", "your name", "bot", "valorbot", "unknown"}
        if parsed.get("name", "").strip().lower() in fake_values:
            return None
        if parsed.get("city", "").strip().lower() in fake_values:
            return None
        if parsed.get("interests") is not None and not isinstance(parsed["interests"], list):
            return None

        if not any(k in parsed for k in ["name", "city", "interests"]):
            return None

        for key, value in parsed.items():
            update_profile(key, value)

            return f"Got it! I've updated your profile with: {', '.join(parsed.keys())}"
        
        else:
            return ""
    
    except Exception as e:
        return f"Couldn't understand what to remember. ({str(e)})"