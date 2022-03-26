import json

with open('data/2022-25-03 12:25:56/San Francisco.json', 'r') as f:
    read = json.load(f)
    print(read.keys())
    print(read['consolidated_weather'][0]["the_temp"])



