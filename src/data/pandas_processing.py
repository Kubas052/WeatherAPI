# data/pandas_processor.py
import pandas as pd
from typing import Dict
from datetime import datetime


class WeatherDataProcessor:
    @staticmethod
    def history_to_dataframe(weather_data: Dict) -> pd.DataFrame:
        """Konwertuje odpowiedź historyczną API na DataFrame"""
        if not weather_data.get('list'):
            raise ValueError("Brak danych w odpowiedzi API")

        # Tworzenie DataFrame
        df = pd.DataFrame([{
            'timestamp': entry['dt'],
            'datetime': pd.to_datetime(entry['dt'], unit='s'),
            'temp': entry['main']['temp'],
            'humidity': entry['main']['humidity'],
            'pressure': entry['main']['pressure'],
            'weather': entry['weather'][0]['main'],
            'wind_speed': entry['wind']['speed']
        } for entry in weather_data['list']])

        return df.set_index('datetime').sort_index()

