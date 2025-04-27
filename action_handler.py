import requests

def execute_task(task):
    if task == "fetch_weather":
        return get_weather()
    elif task == "fetch_news":
        return get_news()
    elif task == "tell_joke":
        return get_joke()
    else:
        return "I'm not sure how to do that yet."

def get_weather():
    # Dummy response for now
    return "The weather is sunny at 25 degrees Celsius."

def get_news():
    # Dummy response for now
    return "Today's headline: AI is transforming the world!"

def get_joke():
    # Dummy response for now
    return "Why did the computer show up late? It had a hard drive!"