import json
import os
from datetime import datetime
from args import dir_

def save_weather(weather, location):
    # создаю папку location если ее нет
    if not os.path.isdir(location):
        os.mkdir(location)

    # создаю внутри location папку с именем по дате
    dir_name = str(datetime.now().strftime("%d_%b_%H:%M"))
    os.makedirs(os.path.join(location, dir_name))

    # записываю все данные по городам в одноименные файлы
    # если изменил директорию, то пишу куда именно сохранил
    for name, weather_data in weather:
        with open(os.path.join(location,dir_name,name + '.json'), 'w') as f:
            json.dump(weather_data, f, indent=4)
            if dir_ == 'data':
                print(f'{name} saved!')
            else:
                print(f'{name} saved into /{dir_}!')

