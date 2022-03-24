import json
import os
from datetime import datetime


def save_weather(weather_data, location):
    if not os.path.isdir(location):
        os.mkdir(location)

    dir_name = str(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
    os.makedirs(f"{location}/{dir_name}")

    for name, weather in weather_data:
        with open(f'{location}/{dir_name}/{name}.json', 'w') as f:
            json.dump(weather, f, indent=4)
            print(f'{name} saved!')
