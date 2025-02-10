import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("Error fetching data from OpenWeatherMap API")

if __name__ == "__main__":
    api_key = "fd9b6bdf315085a3cec8f87f4ddd1779"  # Replace with your OpenWeatherMap API key, sign up on openweather to get your apikey
    city = "London"  # Replace with the city you want to fetch the weather for
    get_weather(api_key, city)

#Code by Ohene Caleb
