# Here we are going to tell whether condition
import requests
from pprint import pprint
import json

API_key = 'c53f3b93f0faaf4a278492979fbc80e4'
city = input('Enter a city:  ')
url = f'https://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}'
res = requests.get(url).text

# This gonna return in json format
deserialize = json.loads(res)
pprint(deserialize)

