import re

def understand_query(query):
    if "weather" in query or "temperature" in query:
        city = extract_city_from_query(query)
        return "fetch_weather", city
    elif "news" in query or "headlines" in query:
        return "fetch_news", None
    elif "joke" in query or "laugh" in query:
        return "tell_joke", None
    else:
        return "unknown", None

def extract_city_from_query(query):
    words = query.split()
    # Simple extraction: assume last word is city if query contains "in"
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            return words[idx + 1]
    return "Delhi"  # default city