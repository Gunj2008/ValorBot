import requests
from config import OPENWEATHER_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "City not found or error fetching weather."
    
    weather = response['weather'][0]['description']
    temp = response['main']['temp']
    return f"The weather in {city} is currently {weather} with a tempreture of {temp}°C."