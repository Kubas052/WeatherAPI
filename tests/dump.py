"""
weather = WeatherAPI().get_current_weather('warsaw')
test30 = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?q=warsaw&dt={timestamp}&units=metric&appid={Config.API_KEY}"
response = requests.get(test30)
print(response.json())

timestamp = int(datetime(2024, 6, 1, 12).timestamp())
weather_api = WeatherAPI()
print(timestamp)
request = f"https://history.openweathermap.org/data/2.5/history/city?q=warsaw&start={timestamp}&end={timestamp + 86400}&appid={Config.API_KEY}&units=metric"
response = requests.get(request)