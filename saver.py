import json
import os
from datetime import datetime


def save_weather(weather, location):
    # создаю папку location если ее нет
    if not os.path.isdir(location):
        os.mkdir(location)

    # создаю внутри location папку с именем по дате
    dir_name = str(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
    os.makedirs(f"{location}/{dir_name}")

    # записываю все данные по городам в одноименные файлы
    for name, weather_data in weather:
        with open(f'{location}/{dir_name}/{name}.json', 'w') as f:
            json.dump(weather_data, f, indent=4)
            print(f'{name} saved!')
