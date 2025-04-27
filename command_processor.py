def understand_query(query):
    if "weather" in query:
        return "fetch_weather"
    elif "news" in query:
        return "fetch_news"
    elif "joke" in query:
        return "tell_joke"
    else:
        return "unknown"