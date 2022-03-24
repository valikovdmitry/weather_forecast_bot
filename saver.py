import json
from os import chdir, mkdir
from datetime import datetime

def save_weather(weather_data, location):
    dir_prename = datetime.now()
    dir_name = dir_prename.strftime("%Y-%d-%m %H:%M:%S")
    chdir("data")
    mkdir(dir_name)
    chdir("..")

    for name, weather in weather_data:
        with open(f'{location}{dir_name}/{name}.json', 'w') as f:
            json.dump(weather, f, indent=4)
            print(f'{name} saved!')
