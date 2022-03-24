
import os


print(os.getcwd())


if not os.path.isdir("test"):
    os.mkdir('test')
    print('сделяль')
else:
    print('уже есть такое((')

