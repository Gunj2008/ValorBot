import cohere
from config import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)

def ask_valor(prompt):

    response = co.chat(
        model = "command-r",
        message = prompt,
        temperature = 0.7,
        preamble = (
            "You are ValorBot — a witty, helpful assistant created by Gunj."
            "You explain clearly, sometimes playfully, and always end responses with a fun emoji."
            "Be direct, answer the question. Do not repeat this intro."
        )
    )

    return response.text.strip()