import os


city = 'Moscow'


def find_city_latest(city, path='data'):
    files = os.listdir(path)
    if files:
        files = [os.path.join(path, file) for file in files]
        dir_path = max(files, key=os.path.getctime)
        dir_files = os.listdir(dir_path)
        if f'{city}.json' in dir_files:
            return dir_path, city


dir_path, city = find_city_latest(city)
