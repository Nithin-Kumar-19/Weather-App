import requests
import datetime

API_KEY = '2842c94e50e05337851b43715f52c9b2'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Failed to get weather data')}")
            return

        city_name = data.get('name')
        country = data.get('sys', {}).get('country')
        temp = data.get('main', {}).get('temp')
        feels_like = data.get('main', {}).get('feels_like')
        temp_min = data.get('main', {}).get('temp_min')
        temp_max = data.get('main', {}).get('temp_max')
        humidity = data.get('main', {}).get('humidity')
        pressure = data.get('main', {}).get('pressure')
        wind_speed = data.get('wind', {}).get('speed')
        wind_deg = data.get('wind', {}).get('deg')
        clouds = data.get('clouds', {}).get('all')
        conditions = data.get('weather', [{}])[0].get('description', '').title()
        dt = datetime.datetime.fromtimestamp(data.get('dt'))

        print(f"\nWeather for {city_name}, {country}")
        print(f"Date & Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Conditions: {conditions}")
        print(f"Temperature: {temp:.1f} °C (feels like {feels_like:.1f} °C)")
        print(f"Min/Max Temperature: {temp_min:.1f} °C / {temp_max:.1f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind: {wind_speed} m/s at {wind_deg}°")
        print(f"Cloud Cover: {clouds}%")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
