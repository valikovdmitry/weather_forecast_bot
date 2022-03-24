import json

def save_weather(weather_data, location):
    for name, weather in weather_data:
        with open(f'{location}{name}.json', 'w') as f:
            json.dump(weather, f, indent=4)
            print(f'{name} saved!')
