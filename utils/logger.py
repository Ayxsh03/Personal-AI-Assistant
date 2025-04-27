def log_conversation(user_query, assistant_response):
    with open("conversation_log.txt", "a") as file:
        file.write(f"User: {user_query}\n")
        file.write(f"Assistant: {assistant_response}\n\n")