# Personal AI Assistant

An intelligent voice-based personal assistant that can:
- Listen to your voice commands
- Predict your intent using Machine Learning
- Fetch latest news headlines
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
