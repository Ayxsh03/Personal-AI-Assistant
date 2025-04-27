import re
import joblib

# Load saved model and vectorizer
model = joblib.load("model/intent_model.pkl")
vectorizer = joblib.load("model/intent_vectorizer.pkl")

def map_intent_to_task(intent):
    if intent == "weather":
        return "fetch_weather"
    elif intent == "news":
        return "fetch_news"
    elif intent == "joke":
        return "tell_joke"
    elif intent == "google":
        return "open_google"
    elif intent == "youtube":
        return "open_youtube"
    elif intent == "search":
        return "search_google"
    elif intent == "open_app":
        return "open_app"
    else:
        return "unknown"
    

def understand_query(query):
    try:
        query_vector = vectorizer.transform([query])
        intent = model.predict(query_vector)[0]
        return map_intent_to_task(intent), None
    except Exception as e:
        print("Error predicting intent:", e)
        return "unknown", None

    
def extract_city_from_query(query):
    words = query.split()
    # Simple extraction: assume last word is city if query contains "in"
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            return words[idx + 1]
    return "Delhi"  # default city

def extract_app_name_from_query(query):
    # Simple regex to find app name
    match = re.search(r"open (.+)", query)
    if match:
        return match.group(1).strip()
    return "default_app"  # default app name

def extract_search_query(query):
    # Simple regex to find search query
    match = re.search(r"search (.+)", query)
    if match:
        return match.group(1).strip()
    return "default_search"  # default search term

def extract_extra_info(query):
    # Extract city or app name based on the task
    if "weather" in query:
        return extract_city_from_query(query)
    elif "open" in query:
        return extract_app_name_from_query(query)
    elif "search" in query:
        return extract_search_query(query)
    else:
        return None
    
def extract_task_and_extra(query):
    task, extra = understand_query(query)
    if task == "fetch_weather":
        extra = extract_city_from_query(query)
    elif task == "open_app":
        extra = extract_app_name_from_query(query)
    elif task == "search_google":
        extra = extract_search_query(query)
    elif task == "fetch_news":
        extra = extract_news_topic(query)
    return task, extra

def extract_news_topic(query):
    """
    Extracts a news topic from user query if mentioned.
    Example: 'Tell me sports news' → topic = 'sports'
    """
    topics = ["sports", "technology", "business", "entertainment", "science", "health", "world", "politics"]

    query = query.lower()

    for topic in topics:
        if topic in query:
            return topic

    return None  # If no specific topic found