import requests
from src.config import Config
from datetime import datetime

class WeatherAPI:
    # WeatherAPI class
    def __init__(self):
        # loading default values
        self.base_url = "https://api.openweathermap.org/data/2.5/"
        self.history_url ="https://history.openweathermap.org/data/2.5/history/"
        self.api_key = Config.API_KEY
    def do_request(self, endpoint, params=None):
        # Common request for endpoints
        params["appid"] = self.api_key
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()
    def get_current_weather(self, city:str):
        return self.do_request("weather", {"q": city, "appid": self.api_key})
    def get_forecast_daily(self, city:str):
        return self.do_request("forecast/daily?", {"q": city, "appid": self.api_key})
    def get_forecast_hourly(self, city:str):
        return self.do_request("forecast/hourly?", {"q": city, "appid": self.api_key})
    def get_history(self, city:str, date: datetime, days:int = 1) -> dict:
        # Only one request, cause there is no endpoint (it has different url, check base_url and history_url)
        start = int(date.timestamp())
        end = start + days*86400
        if days > 7:
            print("max 7 days, reducing to 7 days")
            days = 7
        #adds a day in unix time
        params = {
            "q": city,
            "start": start,
            "end": end,
            "units": "metric",
            "appid": self.api_key
        }
        #basic params from openweather api docs
        response = requests.get(f"{self.history_url}{"city"}", params=params)
        return response.json()

