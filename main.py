from getter import *
from saver import *


# city = input('Type a city: ')
city = 'san '


name_woeid = get_name_woeid(city)

wheather = get_whether(name_woeid)

save_weather(wheather, 'data')
