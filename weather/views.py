from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b96cd015fa463db4e857206ce8405bbc'
    cities = City.objects.all()
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types


        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data}
    return render(request, 'weather/index.html') #returns the index.html template