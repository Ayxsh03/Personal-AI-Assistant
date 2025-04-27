import re
import joblib

# Load saved model and vectorizer
model = joblib.load("model/intent_model.pkl")
vectorizer = joblib.load("model/intent_vectorizer.pkl")

def understand_query(query):
    try:
        query_vector = vectorizer.transform([query])
        intent = model.predict(query_vector)[0]
        return map_intent_to_task(intent), None
    except Exception as e:
        print("Error predicting intent:", e)
        return "unknown", None

def map_intent_to_task(intent):
    if intent == "weather":
        return "fetch_weather"
    elif intent == "news":
        return "fetch_news"
    elif intent == "joke":
        return "tell_joke"
    else:
        return "unknown"

def extract_city_from_query(query):
    words = query.split()
    # Simple extraction: assume last word is city if query contains "in"
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            return words[idx + 1]
    return "Delhi"  # default city