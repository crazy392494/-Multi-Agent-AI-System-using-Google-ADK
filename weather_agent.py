import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(lat, lon):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    return requests.get(url).json()
