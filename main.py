from getter import *
from saver import *


# city = input('Type a city: ')
city = 'san '


name_woeid = get_name_woeid(city)

data = get_whether(name_woeid)

save_weather(data, 'data')
