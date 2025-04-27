from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Dataset: Sample queries and labels
X = [
    # Weather
    "what's the weather",
    "tell me the weather",
    "is it raining outside",
    "weather update for today",

    # News
    "latest news",
    "show me headlines",
    "what happened today",
    "what's new in the world",

    # Jokes
    "tell me a joke",
    "make me laugh",
    "say something funny",
    "I want to hear a joke",

    # Reminders
    "remind me to drink water",
    "set a reminder for meeting",
    "don't let me forget my homework",
    "remind me to call mom",

    # Open Google
    "open google",
    "launch google",
    "go to google website",

    # Open YouTube
    "open youtube",
    "launch youtube",
    "go to youtube website",

    # Search Google
    "search for latest AI news",
    "find top universities",
    "look up best restaurants nearby",

    # Open App
    "open spotify",
    "start calculator app",
    "launch chrome browser",
]

y = [
    # Weather
    "weather",
    "weather",
    "weather",
    "weather",

    # News
    "news",
    "news",
    "news",
    "news",

    # Jokes
    "joke",
    "joke",
    "joke",
    "joke",

    # Reminders
    "reminder",
    "reminder",
    "reminder",
    "reminder",

    # Open Google
    "google",
    "google",
    "google",

    # Open YouTube
    "youtube",
    "youtube",
    "youtube",

    # Search Google
    "search",
    "search",
    "search",

    # Open App
    "open_app",
    "open_app",
    "open_app",
]
# Step 1: Vectorize text
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

# Step 2: Train Classifier
clf = LogisticRegression()
clf.fit(X_vectors, y)

# Step 3: Save Model and Vectorizer
joblib.dump(clf, "model/intent_model.pkl")
joblib.dump(vectorizer, "model/intent_vectorizer.pkl")

print("Model and vectorizer saved successfully!")