import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/weather_db")
CITIES = ["Warsaw", "Berlin", "Paris"]


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        return {
            "city": city,
            "temp": weather["main"]["temp"],
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"],
        }
    print(f"Error fetching data for {city}: {response.status_code}")
    return None


def fetch_all_data():
    return [data for city in CITIES if (data := fetch_weather(city))]


def save_to_csv(data, filename="weather_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return df


def save_to_database(df):
    try:
        engine = create_engine(DB_URL)
        df.to_sql("weather", engine, if_exists="append", index=False)
        print("Data successfully saved to database")
    except Exception as e:
        print(f"Error saving to database: {e}")


if __name__ == "__main__":
    weather_data = fetch_all_data()
    if weather_data:
        df = save_to_csv(weather_data)
        save_to_database(df)