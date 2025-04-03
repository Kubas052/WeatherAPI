class Config:
    API_KEY = '4a225d99df7d676d449cb49b41f8e5c0'
    DEFAULT_CITY = "Warsaw"
    units_options = {
        '1': {'name': 'Celsius (°C)', 'value': 'metric'},
        '2': {'name': 'Fahrenheit (°F)', 'value': 'imperial'},
        '3': {'name': 'Kelvin (K)', 'value': 'standard'}
    }
    default_city = 'Warsaw'
    UNITS = units_options['1']['value']
