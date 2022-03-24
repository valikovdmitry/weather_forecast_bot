import requests


def get_name_woeid(input_city):
    response_cities_data = requests.get('https://www.metaweather.com/api/location/search/', params={'query': input_city})
    cities_data = response_cities_data.json()

    name_woeid = dict()
    for city in cities_data:
        name_woeid[city["title"]] = city['woeid']
    return name_woeid


def get_whether(name_woeid):
    res = dict()
    for name, woeid in name_woeid.items():
        weather_response = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
        weather_data = weather_response.json()

        yield name, weather_data
