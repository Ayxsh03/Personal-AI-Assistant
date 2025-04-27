def understand_query(query):
    if "weather" in query or "temperature" in query:
        return "fetch_weather"
    elif "news" in query or "headlines" in query:
        return "fetch_news"
    elif "joke" in query or "laugh" in query:
        return "tell_joke"
    else:
        return "unknown"