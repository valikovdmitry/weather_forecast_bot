import requests
import json

def get_weather():
    input_ = input('Type your city here: ')

    response_cities_data = requests.get('https://www.metaweather.com/api/location/search/', params={'query': input_})
    cities_data = response_cities_data.json()

    name_woeid = dict()
    for city in cities_data:
        name_woeid[city["title"]] = city['woeid']
    print(name_woeid)

    for name, woeid in name_woeid.items():
        weather_response = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
        weather_data = weather_response.json()
        with open(f'data/{name}.json', 'w') as f:
            json.dump(weather_data, f, indent=4)

