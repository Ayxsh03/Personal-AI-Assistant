from utils.weather_api import get_weather
from utils.news_api import get_latest_news
from utils.jokes_api import get_joke

def execute_task(task, extra=None):
    if task == "fetch_weather":
        return get_weather(extra if extra else "Delhi")
    elif task == "fetch_news":
        return get_latest_news(extra)
    elif task == "tell_joke":
        return get_joke()
    elif task == "open_google":
        open_google()
        return "Opening Google."
    elif task == "open_youtube":
        open_youtube()
        return "Opening YouTube."
    elif task == "open_app":
        app_name = extra if extra else "default_app"
        os.system(f"open -a '{app_name}'")
        return f"Opening {app_name}."
    elif task == "search_google":
        if extra:
            search_google(extra)
        else:
            search_google(extra if extra else "default_search")
        return f"Searching for {extra}."
    else:
        return "I'm not sure how to do that yet."

import os
import webbrowser

def open_google():
    webbrowser.open("https://www.google.com")
def open_youtube():
    webbrowser.open("https://www.youtube.com")
def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
def open_app(app_name):
    os.system(f"open -a '{app_name}'")
