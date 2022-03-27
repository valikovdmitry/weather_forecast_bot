import os


city = 'Moscow'


def find_city_latest(city, path='data'):
    files = os.listdir(path)
    if files:
        files = [os.path.join(path, file) for file in files]
        dir_path = max(files, key=os.path.getctime)
        dir_files = os.listdir(dir_path)
        filtred_files = list(filter(lambda dir_path: city.lower() in dir_path.lower(), dir_files))
        if filtred_files:
            return dir_path, filtred_files[0]


dir_path, city = find_city_latest(city)
