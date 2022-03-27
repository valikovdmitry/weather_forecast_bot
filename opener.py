import json
from find_latest import dir_path, city


def open_weather(dir_path, city):
    with open(f'{dir_path}/{city}.json', 'r') as f:
        reader = json.load(f)
        name = reader['title']
        date = reader['consolidated_weather'][1]['applicable_date']
        state = reader['consolidated_weather'][1]['weather_state_name']
        min_temp = reader['consolidated_weather'][1]['min_temp']
        max_temp = reader['consolidated_weather'][1]['max_temp']


        print(name)
        print(date)
        print(state)
        print(int(min_temp // 1), int(max_temp // 1))


open_weather(dir_path, city)
