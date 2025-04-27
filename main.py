from speech_to_text import listen_to_user
from command_processor import understand_query
from action_handler import execute_task
from text_to_speech import speak

def assistant_loop():
    query = listen_to_user()
    if query:
        task = understand_query(query)
        response = execute_task(task)
        speak(response)

if __name__ == "__main__":
    while True:
        assistant_loop()