import imaplib
import email
from email.header import decode_header
import datetime
from config.settings import COHERE_API_KEY, EMAIL, APP_PASSWORD
import cohere

def clean_header(header_val):
    if header_val:
        return "Unknown"
    
    try:
        decoded, encoding = decode_header(header_val)[0]
        return decoded.decode(encoding or 'utf-8') if isinstance(decoded, bytes) else decoded
    except Exception:
        return str(header_val)

def fetch_recent_emails(limit = 5):
    try:
        print("📡 Connecting to Gmail...")
        mail = imaplib.IMAP4_SSL("imap.gamil.com")
        mail.login(EMAIL, APP_PASSWORD)
        mail.select("inbox")

        date = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%d-%b-%Y")
        print("🕒 Searching since:", date)
        result, data = mail.search(None, 'SINCE', date)

        if result != "OK" or not data or not data[0]:
            raise Exception("No recent emails found.")

        ids = data[0].split()
        recent_ids = ids[-limit:]
        print(f"📬 Found {len(recent_ids)} email(s)")

        emails = []

        for i in recent_ids:
            res, msg = mail.fetch(i, "(RFC822)")

            if res != "OK":
                continue

            raw_email = msg[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = clean_header(msg.get("Subjects"))
            sender = clean_header(msg.get("From"))
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        charset = part.get_content_charset() or 'utf-8'
                        # body = part.get_payload(decode=True).decode(charset, errors="ignore")
                        payload = part.get_payload(decode=True)
                        if payload:
                            body = payload.decode(charset, errors="ignore")
                            break

            else:
                # body = msg.get_payload(decode=True).decode(errors="ignore")
                payload = msg.get_payload(decode=True)
                if payload:
                    body = payload.decode(charset, errors="ignore")

            email.append({
                "from": sender,
                "subject": subject,
                "body": body[:500]
            })

            mail.logout()
            return emails
        
    except Exception as e:
        return [{
            "from": "System",
            "subject": "Error fetching emails",
            "body": f"{type(e).__name__}: {str(e)}"
        }]
    
def summarize_emails(emails):
    if not emails:
        return "No recent emails found."
    
    co = cohere.Client(COHERE_API_KEY)

    combined = "\n\n".join(
        f"From: {email['from']} \nSubject: {email['subject']} \nBody: {email['body']}" for email in emails
    )

    prompt = (
        "You're an assistant summarizing recent emails. Briefly summarize each message in a friendly tone. "
        "Mention who it's from and the subject. Use bullet points."
    )

    response = co.chat(
        model = "command-r",
        message = combined,
        temperature = 0.5,
        chat_history = [],
        preamble = prompt
    )

    return response.text.strip()