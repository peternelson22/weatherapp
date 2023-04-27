from django.shortcuts import render, redirect
import requests
import datetime as dt
from decouple import config
from django.contrib import messages


def index(request):
    api_key = config('API_KEY')
    
    if request.method == 'POST':
        city = request.POST.get('city')
        if city == '':
            return redirect('index')
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        response = requests.get(url)
        json_data = response.json() 

        if json_data['cod'] == '404':
            messages.error(request, 'Not found, pls enter a correct city name')
            return redirect('index')

        data = {'name': json_data['name'], 
                'temp_cl': str(round(json_data['main']['temp'])) + '°C',                
                'temp_fh': str(int((json_data['main']['temp'] * 9/5) + 32)) + '°F',                
                'description': json_data['weather'][0]['description'], 
                'humidity': str(json_data['main']['humidity']) + '%',
                'code': json_data['sys']['country'],
                'date': dt.datetime.utcfromtimestamp(json_data['dt'] + json_data['timezone']),}  
    else:
        data = {}
    return render(request, 'index.html', data)