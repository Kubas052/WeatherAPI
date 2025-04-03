import ui.menu as menu
import core.api as api

if __name__ == "__main__":
    weather_api = api.WeatherAPI()
    menu = menu.Menu(weather_api)
    menu.run()