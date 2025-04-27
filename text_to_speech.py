import pyttsx3
import random

engine = pyttsx3.init()

def speak(text):
    friendly_phrases = ["Here's what I found:", "Alright!", "Got it!", "Okay, listen:"]
    if not text.startswith("Sorry"):
        intro = random.choice(friendly_phrases)
        text = f"{intro} {text}"
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()