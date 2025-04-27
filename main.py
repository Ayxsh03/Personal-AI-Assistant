from speech_to_text import listen_to_user
from command_processor import understand_query
from action_handler import execute_task
from text_to_speech import speak
from utils.logger import log_conversation
import speech_recognition as sr

def assistant_loop():
    query = listen_to_user()
    if query:
        task, extra = understand_query(query)
        response = execute_task(task, extra)
        log_conversation(query, response)  # log here
        if response == "I'm not sure how to do that yet.":
            speak("Sorry, I don't know how to help with that yet. Can you try again?")
        else:
            speak(response)

def wait_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'Hey Assistant' to start...")
        audio = recognizer.listen(source)
    try:
        wake_query = recognizer.recognize_google(audio).lower()
        return "hey assistant" in wake_query
    except:
        return False

if __name__ == "__main__":
    while True:
        if wait_for_wake_word():
            assistant_loop()