from src.data.pandas_processing import WeatherDataProcessor
from src.core.api import WeatherAPI


class Menu:
    def __init__(self, weather_api):
        self.weather_api = WeatherAPI
        self.data_process = WeatherDataProcessor
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
            "5": self.run
        }
        self.settings_submenu_options = {
            "1": self.change_temperature,
            "2": self.change_main_city,
            "3": self.run
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
        print("4. maps")
        print("5. Powrót")

    def display_settings_submenu(self):
        print("\nPODMENU 2:")
        print("1. Change temperature system")
        print("2. Change main city")
        print("3. Powrót")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Wybierz opcję: ")
            action = self.main_options.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def weather_submenu(self):
        while True:
            self.display_weather_submenu()
            choice = input("Wybierz opcję: ")
            action = self.weather_submenu_options.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def settings_submenu(self):
        while True:
            self.display_settings_submenu()
            choice = input("Wybierz opcję: ")
            action = self.settings_submenu_options.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def today_weather(self):
        request_city = input("please input city name: ")
        print(self.weather_api.get_current_weather(request_city))

    def forecast_weather(self):
        print("forecast")

    def historical_weather(self):
        print("historical")

    def maps(self):
        print("maps")

    def change_temperature(self):
        print("temperature")

    def change_main_city(self):
        print("main city")

    def exit_program(self):
        print("Zamykanie programu...")
        exit()


if __name__ == "__main__":
    menu = Menu()
    menu.run()