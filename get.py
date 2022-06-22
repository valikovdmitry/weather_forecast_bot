import requests
from main import API_KEY_OPENWEATHER


def get_whether(city):
    weather_response = requests.get('https://api.openweathermap.org/data/2.5/forecast',
                                    params={"q": f"{city}", "cnt": 10, "appid": f"{API_KEY_OPENWEATHER}",
                                            "units": "metric"})
    weather_data = weather_response.json()

    return weather_data
