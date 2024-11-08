# utils/transform.py
import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    df['played_at'] = pd.to_datetime(df['played_at'])
    df['duration_min'] = df['duration_ms'] / 60000  # Convertir duración a minutos
    return df