# cначала импорты внешние потом внутр(алф пор), фромы внешние потом внутр(алф пор), константы, функции
from get_args import get_args
from getter import *
from path_manager import PathManager


DEFAULT_LOCATION = 'data' # глобальные переменные которые не меняются - КОНСТАНТА - пишем все апперкейсом


def main(city, manager):  # это скрипт
    name_woeid = get_name_woeid(city)
    wheather = get_whether(name_woeid)
    manager.save_weather(wheather)
    manager.print_weather(city)




if __name__ == '__main__':
    city, dir_ = get_args()
    manager = PathManager(dir_)
    main(city, manager)
