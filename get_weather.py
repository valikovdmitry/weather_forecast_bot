import requests


def find_cities_and_id(input_city):
    response_cities_data = requests.get('https://www.metaweather.com/api/location/search/', params={'query': input_city})
    cities_data = response_cities_data.json()

    name_woeid = dict()
    for city in cities_data:
        name_ = city["title"]
        name_woeid[city["title"]] = city['woeid']
    return name_woeid, name_


def get_whether_data(x):
    res = []
    for name, woeid in x.items():
        weather_response = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')
        weather_data = weather_response.json()


        yield name, weather_data
