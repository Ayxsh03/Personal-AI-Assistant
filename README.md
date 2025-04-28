![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Windows-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202025-blueviolet.svg)
# 🦾Personal AI Assistant

An intelligent voice-based personal assistant that can:
- Listen to your voice commands
- Predict your intent using Machine Learning
- Fetch the latest news headlines
- Fetch weather information
- Tell jokes
- Open apps or websites
- Perform Google searches
- Speak back natural responses
- Learn and expand easily!

Built with Python 🐍 | Speech Recognition | Machine Learning | APIs | Text-to-Speech.

---

## 🚀 Features

- 🎤 **Speech-to-Text**: Listens to your microphone input
- 🧠 **ML-based Intent Detection**: Classifies commands like weather, news, jokes, open apps
- 📢 **Text-to-Speech**: Replies back with friendly speech
- 🌦️ **Weather Reports**: Fetches real-time weather
- 📰 **News Headlines**: Fetches top news or specific category news (sports, tech, etc.)
- 🤣 **Joke Teller**: Tells random jokes
- 🌐 **Open Apps**: Launches apps and websites on command
- 📝 **Conversation Logging**: Saves conversation history to a file
- 👂 **Wake Word Detection**: Activates on "Hey Assistant"
- 🛠️ **Modular Code**: Easy to add more skills and APIs!

---

## 🎯 Example Commands

Here are some voice commands you can try with the Assistant:

| 🗣️ You Say | 🤖 Assistant Action |
|:---|:---|
| "Tell me the latest news" | Fetches and speaks today's top headlines |
| "Show me sports news" | Fetches and speaks top sports news |
| "What's the weather in Delhi?" | Tells the weather update for Delhi |
| "Will it rain today?" | Gives current weather forecast |
| "Tell me a joke" | Speaks a random joke to make you laugh |
| "Open Google" | Opens Google.com in your web browser |
| "Open YouTube" | Opens YouTube.com in your web browser |
| "Open Spotify" | Launches the Spotify application |
| "Search Google for best AI projects" | Performs a Google search for 'best AI projects' |
| "Remind me to drink water" | (Planned) Create a future reminder |
| "Play my favourite song" | (Planned) Play music from your local system |


## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Ayxsh03/Personal-AI-Assistant.git
cd Personal-AI-Assistant
```
2.	**Install required packages**
    ```bash
    pip install -r requirements.txt
    ```
3. **Set up API Keys**

   Replace placeholders inside /utils/weather_api.py and /utils/news_api.py with your real API keys:
   - OpenWeatherMap API
	- GNews API

5. **Train the ML model**
   ```bash
   python model/train_intent_classifier.py
   ```
   
6. **Run the Assistant**
   ```bash
   python main.py
   ```

## 🗂️Folder Structure
```bash
Personal-AI-Assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  
│   ├── assistant_core.py         
│   ├── command_processor.py      
│   ├── action_handler.py         
│   ├── text_to_speech.py         
│   ├── speech_to_text.py        
│
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── weather_api.py   
│   │   ├── news_api.py          
│   │   ├── jokes_api.py        
│   │   └── logger.py              
│
│   ├── model/
│   │   ├── __init__.py
│   │   ├── intent_model.pkl       
│   │   ├── intent_vectorizer.pkl  
│
├── requirements.txt
├── README.md
└── LICENSE (optional)
   ```

## 📈Assistant Flow Diagram
```bash
User (Mic Input)
      ↓
Speech-to-Text (speech_recognition)
      ↓
User Query (text)
      ↓
ML Model (intent_model.pkl)
      ↓
Predicted Intent 
      ↓
Action Handler
      ↓ 
Executes Query OR Fetches API
      ↓
Text Response
      ↓
Text-to-Speech (pyttsx3)
      ↓
Assistant speaks response
```
