import requests

API_KEY = "5780fa4eacd1d04a9b7da15f87cc4e15"

def get_weather(city="Delhi"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return "Sorry, I couldn't fetch the weather."
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    except Exception as e:
        print(e)
        return "Failed to fetch weather."