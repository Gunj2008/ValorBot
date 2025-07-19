import cohere
from config.settings import COHERE_API_KEY

chat_memory = []

def get_chat_memory():
    return chat_memory

def clear_chat_memory():
    chat_memory.clear()

def handle_multi_turn(user_input):
    co = cohere.Client(COHERE_API_KEY)

    history_formatted = []

    for turn in chat_memory:
        history_formatted.append({'role' : "USER", 'message' : turn["user"]})
        history_formatted.append({'role' : "CHATBOT", 'message' : turn["bot"]})

    response = co.chat(
        model = "command-r",
        message = user_input,
        temperature = 0.6,
        chat_history = history_formatted
    )

    bot_reply = response.text.strip()
    chat_memory.append({"user" : user_input, "bot" : bot_reply})
    return bot_reply