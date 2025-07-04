# ValorBot – Your Intelligent Personal Assistant

**ValorBot** is an AI-powered personal assistant built with Python and Cohere's LLMs. It understands natural language, remembers your preferences, gives weather updates, manages your to-do list, and learns about you over time.

> 🧠 Powered by Cohere's `command-r` chat model  
> 💾 Remembers your name, city, and interests  
> 🌤️ Supports plugins for weather, to-do, and more  
> 🛡️ Fully modular, secure, and environment-ready

---

## 🏗️ Features

- 🧠 **LLM-based memory system** – Remembers user info like name, city, and interests from natural language
- ⛅ **Weather plugin** – Gets current weather using OpenWeather API
- ✅ **To-do manager** – Add and show personal tasks
- 💬 **Conversational AI** – Uses Cohere chat model to handle questions and fallback responses
- 🔐 **Secure config** – API keys stored in `.env`, loaded via `python-dotenv`
- 🗂️ **Modular folder structure** – Easy to expand with new plugins
- 🧪 **Debug friendly** – Includes raw output logging for LLM responses

---

## 🧰 Tech Stack

| Tool        | Purpose                         |
|-------------|----------------------------------|
| Python      | Core language                    |
| Cohere      | Chat model for AI interaction    |
| OpenWeather | Weather data                     |
| `dotenv`    | Secure config management         |
| JSON        | Persistent memory store          |

---

## 📁 Project Structure

```
ValorBot/
│
├── main.py                  # CLI entry point
├── .env                     # API keys (excluded from Git)
├── requirements.txt
│
├── config/
│   └── settings.py          # Loads API keys via dotenv
│
├── Assistants/
│   ├── chat.py              # Core AI response
│   └── plugins/
│       ├── memory.py        # Load/save profile
│       ├── memory_parser.py # LLM-based memory extractor
│       ├── todo.py          # Task manager
│       └── weather.py       # Weather fetcher
│
├── data/
│   └── user_profile.json    # User memory (persistent)
```

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Gunj2008/ValorBot.git
cd ValorBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
COHERE_API_KEY=your-cohere-key
OPENWEATHER_API_KEY=your-openweather-key
```

### 4. Run the bot

```bash
python main.py
```

---

## 🔒 `.env` Example

Make sure to keep this file **secret** and **excluded from Git**!

```env
COHERE_API_KEY=your-cohere-key-here
OPENWEATHER_API_KEY=your-openweather-api-key-here
```

---

## 🌱 Roadmap

- [x] Smart memory parsing via LLM
- [x] Natural language task manager
- [x] Weather plugin
- [ ] Add voice input/output
- [ ] Add daily summary feature
- [ ] Add news/joke plugins
- [ ] Build a web or TUI interface

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙌 Credits

- [Cohere](https://cohere.com) – for the amazing LLM
- [OpenWeather](https://openweathermap.org) – for weather data
- Built by **@Gunj2008** and ValorBot ✨