# Weather Application 🌦️

A Python-based weather application that provides current, forecast, and historical weather data using OpenWeatherMap API.

## Features ✨

- Current weather conditions for any city
- Weather forecast (daily and hourly)
- Historical weather data
- Interactive maps
- Temperature unit conversion (Celsius/Fahrenheit)
- Configurable main city

## Technologies Used 🛠️

- Python 3.x
- Requests (for API calls)
- pandas (for data processing)
- python-dotenv (for environment variables)

## Future Development 🚧
- Matplotlib weather charts
- API response caching
- JSON/CSV data export
- map tile integration (satellite/radar via API)
- multi-language support

## Project Structure 📂
```
WeatherAPI/
├── .venv/                     
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   └── api.py            # Core API
│   ├── data/
│   │   ├── __init__.py
│   │   └── pandas_processing.py  # Przetwarzanie danych
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── graphs.py         # work in progress
│   │   ├── menu.py           # Menu interface
│   │   └── prompts.py        # work in progress
│   ├── __init__.py           
│   ├── config.py             # Config file (change API_KEY here!)
│   └── .env                  # API_KEY file (gitignore)
├── .gitignore                
├── README.md                 # Docs
└── main.py                   # Main app
```
