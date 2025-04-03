from src.data.pandas_processing import WeatherDataProcessor
from src.core.api import WeatherAPI
from datetime import datetime


class Menu:
    def __init__(self, weather_api):
        self.weather_api = weather_api  # Używamy przekazanego obiektu zamiast klasy
        self.data_processor = WeatherDataProcessor()  # Inicjujemy obiekt
        self.main_options = {
            "1": self.weather_submenu,
            "2": self.settings_submenu,
            "3": self.exit_program
        }
        self.weather_submenu_options = {
            "1": self.today_weather,
            "2": self.forecast_weather,
            "3": self.historical_weather,
            "4": self.maps,
            "5": self.back_to_main
        }
        self.settings_submenu_options = {
            "1": self.change_temperature,
            "2": self.change_main_city,
            "3": self.back_to_main
        }

    def display_main_menu(self):
        print("\nMAIN MENU:")
        print("1. Weather Submenu")
        print("2. Settings")
        print("3. Exit")

    def display_weather_submenu(self):
        print("\nWeather Submenu:")
        print("1. Today's Weather")
        print("2. Forecast weather")
        print("3. Historical weather")
        print("4. Maps")
        print("5. Back to main menu")

    def display_settings_submenu(self):
        print("\nSETTINGS SUBMENU:")
        print("1. Change temperature system")
        print("2. Change main city")
        print("3. Back to main menu")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Choose option: ")
            action = self.main_options.get(choice)
            if action:
                action()
            else:
                print("Invalid option, try again.")

    def weather_submenu(self):
        while True:
            self.display_weather_submenu()
            choice = input("Choose option: ")
            action = self.weather_submenu_options.get(choice)
            if action:
                action()
                if choice == "5":
                    break
            else:
                print("Invalid option, try again.")

    def settings_submenu(self):
        while True:
            self.display_settings_submenu()
            choice = input("Choose option: ")
            action = self.settings_submenu_options.get(choice)
            if action:
                action()
                if choice == "3":
                    break
            else:
                print("Invalid option, try again.")

    def today_weather(self):
        request_city = input("Please input city name: ")
        weather_data = self.weather_api.get_current_weather(request_city)
        print(weather_data)

    def forecast_weather(self):
        request_city = input("Please input city name: ")
        weather_data = self.weather_api.get_forecast_daily(request_city)
        print(weather_data)

    def historical_weather(self):
        request_city = input("Please input city name: ")
        date_str = input("Please input date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            days = int(input("How many days (max 7)? "))
            weather_data = self.weather_api.get_history(request_city, date, days)
            print(weather_data)
        except ValueError:
            print("Invalid date format or days number")

    def maps(self):
        print("Maps functionality will be implemented here")

    def change_temperature(self):
        current_unit = "Celsius"  # wrzuc do cinfiga
        print(f"Current temperature unit: {current_unit}")
        new_unit = input("Change to (C/F): ").upper()
        if new_unit in ["C", "F"]:
            print(f"Temperature unit changed to {'Celsius' if new_unit == 'C' else 'Fahrenheit'}")
            # Zrob zmiane jednostek config
        else:
            print("Invalid unit, must be C or F")

    def change_main_city(self):
        current_city = "Warsaw"  # To powinno być przechowywane w konfiguracji
        print(f"Current main city: {current_city}")
        new_city = input("Enter new main city: ")
        if new_city:
            print(f"Main city changed to {new_city}")
            # Zrob logike na zmiane miasta w configu

    def back_to_main(self):
        """Helper method to go back to main menu"""
        pass

    def exit_program(self):
        print("Closing program...")
        exit()