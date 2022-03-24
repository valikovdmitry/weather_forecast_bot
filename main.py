from getter import *
from saver import *


city = input('Type a city: ')


name_woeid = get_name_woeid(city)

data = get_whether(name_woeid)

save_weather(data, 'data/')
