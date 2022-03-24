import get_weather
import save_weather

city = 'san '

woeid, name = get_weather.find_cities_and_id(city)
print(woeid, name)

data = get_weather.get_whether_data(woeid)
print(data)

for name, weather in data:
    print(name, weather)

save_weather.save_weather(data)