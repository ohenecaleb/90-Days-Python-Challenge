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
        temperature = data['main']['temp'] #Refer to Nested dictionary for more understanding
        weather = data['weather'][0]['description']#Refer to Nested dictionary for more understanding
        
    
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")
    else:
        print("Error fetching data from OpenWeatherMap API")
        print(f"Response Content: {response.text}")

if __name__ == "__main__":
    api_key = "fd9b6bdf315085a3cec8f87f4ddd1779"  # Replace with your OpenWeatherMap API key
    city = "New York"  # Replace with the city you want to fetch the weather for
    get_weather(api_key, city)


    # You can get your API key by signing up on OpenWeatherMap and generating a new API key.
    # Code By Ohene Caleb
