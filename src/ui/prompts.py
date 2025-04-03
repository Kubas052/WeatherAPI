
class Menu:
    def __init__(self):
        self.main_options = {
            "1": self.weather_submenu,
            "2": self.settings_submenu,
            "3": self.exit_program()
        }
        self.weather_submenu = {
            "1": self.option_one_one,
            "2": self.option_one_two,
            "3": self.run
        }
        self.settings_submenu = {
            "1": self.option_two_one,
            "2": self.option_two_two,
            "3": self.run
        }

    def display_main_menu(self):
        print("\nMain Menu:")
        print("1. Weather 1")
        print("2. Settings 2")
        print("3. Exit")

    def display_weather_submenu(self):
        print("\nPODMENU 1:")
        print("1. Opcja 1.1")
        print("2. Opcja 1.2")
        print("3. Powrót")

    def display_settings_submenu(self):
        print("\nPODMENU 2:")
        print("1. Opcja 2.1")
        print("2. Opcja 2.2")
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
            action = self.weather_submenu.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def settings_submenu(self):
        while True:
            self.display_settings_submenu()
            choice = input("Wybierz opcję: ")
            action = self.settings_submenu.get(choice)
            if action:
                action()
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

    def option_one_one(self):
        print("Wybrano opcję 1.1!")

    def option_one_two(self):
        print("Wybrano opcję 1.2!")

    def option_two_one(self):
        print("Wybrano opcję 2.1!")

    def option_two_two(self):
        print("Wybrano opcję 2.2!")

    def exit_program(self):
        print("Zamykanie programu...")
        exit()


menu = Menu()
menu.run()