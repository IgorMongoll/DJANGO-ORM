from django.core.management.base import BaseCommand
import requests
class Command(BaseCommand):

    def handle(self, *args, **options):
        # this is where we get infor from the API
        print("Hello, I work!!")
        url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
        data = requests.get(url)
        print(data)        
        current_weather = data.json().get('current_weather')
        longitude = data.json().get('longitude')
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        time = current_weather['time']
        print(longitude)      
        print(temperature)
        print(windspeed)
        # Weather.objects.create(temperature=temperature, time=time, windspeed=windspeed)