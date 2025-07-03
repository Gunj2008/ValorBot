import cohere
from config.settings import COHERE_API_KEY
from Core.prompt_template import get_system_prompt

co = cohere.Client(COHERE_API_KEY)

def ask_valor(prompt):

    response = co.chat(
        model = "command-r",
        message = prompt,
        temperature = 0.7,
        preamble = get_system_prompt()
    )

    return response.text.strip()