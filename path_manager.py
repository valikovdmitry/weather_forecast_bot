import json
import os
from datetime import datetime


class PathManager:
    def __init__(self, path):
        self.path = path
        self.create_path()

    def create_path(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def save_weather(self, weather):
        dir_name = str(datetime.now().strftime("%d_%b_%H:%M"))
        os.makedirs(os.path.join(self.path, dir_name))

        for name, weather_data in weather:
            with open(os.path.join(self.path, dir_name, name + '.json'), 'w') as f:
                json.dump(weather_data, f, indent=4)
                print(f'{name} saved!')

    def find_city_latest(self, city):
        files = os.listdir(self.path)
        if files:
            files = [os.path.join(self.path, file) for file in files]
            dir_path = max(files, key=os.path.getctime)
            dir_files = os.listdir(dir_path)
            filtred_files = list(filter(lambda dir_path: city.lower() in dir_path.lower(), dir_files))
            if filtred_files:
                return dir_path, filtred_files[0]
            # добавить элсе

    def open_weather(self, city):
        dir_path, city_file = self.find_city_latest(city)
        with open(f'{dir_path}/{city_file}', 'r') as f:
            data = json.load(f)

        return data

    def print_weather(self, city):
        data = self.open_weather(city)
        name = data['title']
        date = data['consolidated_weather'][1]['applicable_date']
        state = data['consolidated_weather'][1]['weather_state_name']
        min_temp = data['consolidated_weather'][1]['min_temp']
        max_temp = data['consolidated_weather'][1]['max_temp']

        print(name)
        print(date)
        print(state)
        print(int(min_temp // 1), int(max_temp // 1))
