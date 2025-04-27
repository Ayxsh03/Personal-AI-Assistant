from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Dataset: Sample queries and labels
X = [
    "what's the weather",
    "tell me the weather",
    "will it rain today",
    "latest news headlines",
    "show me some news",
    "what's in the news",
    "tell me a joke",
    "make me laugh",
    "say something funny",
]
y = [
    "weather",
    "weather",
    "weather",
    "news",
    "news",
    "news",
    "joke",
    "joke",
    "joke",
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