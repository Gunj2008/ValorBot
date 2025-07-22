# 🤖 ValorBot

**ValorBot** is your personal AI-powered assistant that can help with:

- ✅ Natural conversations (chat)
- 📧 Email summarization (Gmail)
- ⛅️ Weather updates
- 📝 To-do tasks
- 🗃️ Memory & profile updates
- 🔊 Voice interaction (input/output)
- 📄 PDF & DOCX summarization
- 🧠 Multi-turn memory

Powered by [Cohere](https://cohere.com), OpenWeather, and other powerful libraries, ValorBot is your always-ready assistant on desktop or the web.

---

## ✨ Features

- 💬 Conversational AI with memory
- 🧠 Remembers your name, city, interests
- 🗃️ Multi-turn memory with history
- 📥 Email fetching and summarization from Gmail
- 📄 PDF / DOCX summarizer
- 📝 Add and show to-do tasks
- 🎤 Voice input + TTS reply (offline or gTTS)
- ⛅️ Weather information using OpenWeather
- 🖥️ Web UI using Gradio
- 💠 Modular codebase with plugin architecture

---

## 📁 Project Structure

```
ValorBot/
|
├── Assistants/
│   ├── chat.py              # Core Q&A logic
│   ├── memory.py            # Profile memory system
│   ├── memory_parser.py     # Cohere memory extractor
│   ├── weather.py           # Weather plugin
│   ├── todo.py              # To-do manager
│   ├── voice_io.py          # Speech-to-text / TTS
│   ├── email_summary.py     # Email summarizer (Gmail)
│   ├── doc_summary.py       # PDF / DOCX summarizer
│   └── conversation.py      # Multi-turn conversation state
│
├── config/
│   └── settings.py          # API keys loaded from .env
│
├── Core/
│   └── prompt_template.py   # System prompt template
│
├── main.py                  # CLI voice/terminal app
├── app.py                   # Gradio web app
├── requirements.txt
└── README.md
```

---

## 💠 Installation

### 1. Clone the repo

```bash
git clone https://github.com/Gunj2008/ValorBot.git
cd ValorBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the `config/` directory:

```ini
# config/.env
COHERE_API_KEY=your_cohere_key
OPENWEATHER_API_KEY=your_weather_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
```

> 💡 Make sure "Less Secure Apps" or App Passwords are configured for Gmail.

---

## 🦖 Running the App

### 🖥️ CLI Mode

```bash
python main.py
```

You will be prompted:

```
Do you want to use voice mode ? (y/n):
```

### 🌐 Web App (Gradio)

```bash
python app.py
```

Then open [http://localhost:7860](http://localhost:7860) in your browser.

---

## 📄 File Summarization

You can summarize local files with:

```bash
> summarise file path/to/document.pdf
```

Supported formats: `.pdf`, `.docx`

---

## ✨ Examples

```bash
> What is the weather in Mumbai?
> Add task Buy groceries
> Summarise my inbox
> Show my memory
> What is an AI?
```

---

## 🤝 Contributing

PRs are welcome! If you’d like to add a plugin or improve the UI, feel free to fork and submit a pull request.

---

## 🧠 Credits

Built with ❤️ by [**Gunj2008**](https://github.com/Gunj2008) using:

- [Cohere](https://cohere.com)
- [OpenWeather](https://openweathermap.org)
- [Gradio](https://gradio.app)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

---

## 📌 License

This project is under the **MIT License**. See [LICENSE](LICENSE) for more.

