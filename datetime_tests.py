


import datetime
from os import mkdir, chdir

dir_prename = datetime.datetime.now()
dir_name = dir_prename.strftime("%Y-%d-%m %H:%M:%S")


chdir("data")
mkdir(dir_name)
chdir("..")

print(dir_name)


