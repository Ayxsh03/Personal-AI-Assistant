import pyttsx3
import random

engine = pyttsx3.init()

# List available voices (only once, comment later)
voices = engine.getProperty('voices')

# Set desired Siri-like female voice (Samantha)
for voice in voices:
    if "samantha" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Optional: Set speech rate (speed)
engine.setProperty('rate', 170)  # default ~200 wpm

# Optional: Set volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

def speak(text):
    friendly_phrases = ["Here's what I found:", "Alright!", "Got it!", "Okay, listen:"]
    if not text.startswith("Sorry"):
        intro = random.choice(friendly_phrases)
        text = f"{intro} {text}"
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()