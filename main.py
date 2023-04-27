import requests
from pprint import pprint


API_KEY = '6ba6568e97173d67b639301722e25382'

city = input('Enter city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}'

response = requests.get(url)

pprint(response.json())

if response.status_code == 200:
    data = response.json()
    name = data['name']
    temp = data['main']['temp']

    print(f'The temperature of {name} is {round(temp)}℉')

else:
    print(f'Sorry we can\'t give the details of {city}')