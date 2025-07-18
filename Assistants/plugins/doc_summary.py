import fitz
from docx import Document
from config.settings import COHERE_API_KEY
import cohere

co = cohere.Client(COHERE_API_KEY)

def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)

    for page in doc:
        text += page.get_text()

    return text.strip()

def extract_text_from_doc(path):
    text = ""
    doc = Document(path)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text.strip()

def summarise_text(text, max_tokens = 1000):
    if not text:
        return "No text found to summarise."
    
    trimmed = text[:4000]

    prompt = (
        "You're an AI assistant that summarizes documents. Provide a clear, concise summary of the following text:\n\n"
        + trimmed
    )

    response = co.chat(
        model = "command-r",
        message = prompt,
        temperature = 0.4,
        chat_history = [],
    )

    return response.text.strip()