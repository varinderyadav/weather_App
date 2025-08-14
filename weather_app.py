import requests

API_KEY = "cbd1d47361b75690ebde71f00a439949"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Always include country code for better accuracy
        url = f"{BASE_URL}?q={city},IN&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.title()}")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found. Please check the name and try again.")
        elif response.status_code == 401:
            print("Invalid API key. Please check your OpenWeatherMap API key.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
