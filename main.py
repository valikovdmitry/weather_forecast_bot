# cначала импорты внешние потом внутр(алф пор), фромы внешние потом внутр(алф пор), константы, функции
from get_args import city, dir_
from getter import *
from saver import *


DEFAULT_LOCATION = 'data' # глобальные переменные которые не меняются - КОНСТАНТА - пишем все апперкейсом


def main(city, location = DEFAULT_LOCATION):  # это скрипт
    name_woeid = get_name_woeid(city)
    wheather = get_whether(name_woeid)
    save_weather(wheather, location)


if __name__ == '__main__':
    main(city, dir_)
