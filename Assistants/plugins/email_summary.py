from imapclient import IMAPClient
import pyzmail
import datetime
import ssl
import cohere
from config.settings import COHERE_API_KEY, EMAIL, APP_PASSWORD

def fetch_recent_emails(limit = 5):
    context = ssl.create_default_context()
    server = IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
    server.login(EMAIL, APP_PASSWORD)
    server.select_folder("INBOX", readonly=True)

    since = datetime.datetime.now() - datetime.timedelta(days=3)
    messages = server.search(["SINCE"], since.strftime("%d-%b-%Y"))

    fetched = server.fetch(messages, ["BODY[]", "FLAGS"])
    emails = []

    for uid in sorted(fetched.keys(), reverse=True)[:limit]:
        msg = pyzmail.PyzMessage.factory(fetched[uid][b"BODY[]"])
        subject = msg.get_subject()
        sender = msg.get_addresses("from")[0][1]
        text = msg.text_part.get_payload().decode() if msg.text_part else ""
        emails.append({
            "from": sender,
            "subject": subject,
            "text": text
        })

    server.logout()
    return emails
    
def summarise_emails(emails):
    if not emails:
        return "No recent emails to summarise."
    
    co = cohere.Client(COHERE_API_KEY)

    combined_text = "\n\n".join(
        f"From: {e['from']} \nSubject: {e['subject']} \nBody: {e['body'][:500]}" for e in emails
    )

    system_prompt = (
        "You're a helpful assistant. Summarize the following emails briefly. "
        "Use bullet points and mention the sender and subject where relevant."
    )

    response = co.chat(
        model = "command-r",
        maessage = combined_text,
        temperature = 0.5,
        chat_history = [],
        preamble = system_prompt
    )

    return response.text.strip()