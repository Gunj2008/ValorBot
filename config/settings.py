import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

if __name__ == "__main__":
    print("COHERE_API_KEY:", COHERE_API_KEY)
    print("OPENWEATHER_API_KEY:", OPENWEATHER_API_KEY)
    print("EMAIL:", EMAIL)
    print("APP_PASSWORD:", APP_PASSWORD)