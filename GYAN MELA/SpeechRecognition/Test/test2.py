import requests
from command_list import commands
text = 'hey what is the weather in banglore'.split()
print(text)

def getWeather(city_name):
    API_KEY = "f354c11eb850918547081c684e06e42d"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    city = city_name
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)

        return weather, temperature
    else:
        return 0

def query_filter(text):
    for word in text:
        if word in commands:
            print('There is a word! The word is ' + word)
            text.remove(word)
        
    return text

city = query_filter(text)
city.remove('weather')
print(city)
for i in range(len(city)):
    print(city[i])