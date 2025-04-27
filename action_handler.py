from utils.weather_api import get_weather
from utils.news_api import get_latest_news
from utils.jokes_api import get_joke

def execute_task(task, extra=None):
    if task == "fetch_weather":
        return get_weather(extra if extra else "Delhi")
    elif task == "fetch_news":
        return get_latest_news()
    elif task == "tell_joke":
        return get_joke()
    else:
        return "I'm not sure how to do that yet."