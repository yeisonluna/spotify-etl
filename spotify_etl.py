# etl.py
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from config.config import get_spotify_client
from utils.spotify_api import get_recently_played
from utils.transform import transform_data

# Cargar las variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def load_to_postgres(df):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/spotify_db")
    df.to_sql('spotify_tracks', engine, if_exists='append', index=False)

def run_etl():
    sp = get_spotify_client()
    raw_data = get_recently_played(sp)
    df = transform_data(raw_data)
    load_to_postgres(df)

if __name__ == "__main__":
    run_etl()
