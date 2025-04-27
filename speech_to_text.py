import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Error recognizing speech:", str(e))
        return 