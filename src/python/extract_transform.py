import os
from dotenv import load_dotenv
import pandas as pd
import requests
import pandas

load_dotenv()   # Load variable from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# List of cities
CITIES = ["Warsaw", "Berlin", "Paris"]

def fetch_data():
    data = []
    for city in CITIES:
        API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(API_URL.format(city=city))
    if response.status_code == 200:
        data.append({
            "city": city,
            "temp": response.json()["main"]["temp"],
            "humidity": response.json()["main"]["humidity"]
        })
    else:
        print(f"Error for city {city}: {response.status_code}")

        df = pd.DataFrame(data)
        df.to_csv("weather_data.csv", index=False)

if __name__ == "__main__":
    fetch_data()