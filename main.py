from speech_to_text import listen_to_user
from command_processor import understand_query
from action_handler import execute_task
from text_to_speech import speak
from utils.logger import log_conversation
import speech_recognition as sr
from command_processor import extract_task_and_extra


def assistant_loop():
    query = listen_to_user()
    if query:
        task, extra = extract_task_and_extra(query)
        response = execute_task(task, extra)
        log_conversation(query, response)  # log here
        if response == "I'm not sure how to do that yet.":
            speak("Sorry, I don't know how to help with that yet. Can you try again?")
        else:
            speak(response)

def wait_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Hey Assistant' to activate...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            wake_query = recognizer.recognize_google(audio).lower()
            if "hey assistant" in wake_query:
                return True
            else:
                print("Didn't hear wake word. Listening again...")
                return False
        except:
            print("Listening timeout, retrying...")
            return False


import datetime

def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good Morning, Ayush!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Ayush!")
    else:
        speak("Good Evening, Ayush!")

if __name__ == "__main__":
    greet_user()
    while True:
        if wait_for_wake_word():
            assistant_loop()