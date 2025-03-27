from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://user:password@localhost:5432/weather_db")
df = pd.read_csv("weather_data.csv")
df.to_sql("weather", engine, if_exists="append", index=False)