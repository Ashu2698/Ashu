import requests

def get_weather(location):
    api_key = '1a7819f6903571f4e64e679aece81070'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == 200:
        print(f"Weather in {data['name']}:")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error:", data['message'])

def main():
    location = input("Enter location (city name): ")
    weather_data = get_weather(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
