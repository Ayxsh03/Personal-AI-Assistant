import requests

API_KEY = "3ccd6f2b75696aa8afc4cf3541844415"
GNEWS_API_URL = "https://gnews.io/api/v4/top-headlines"

def get_latest_news(topic=None):
    """
    Fetch latest news headlines using GNews API.
    """

    try:
        if not API_KEY:
            return "News API key is not configured."

        params = {
            "token": API_KEY,
            "lang": "en",
            "max": 5,  # Limit to 5 articles
        }

        if topic:
            params["q"] = topic

        response = requests.get(GNEWS_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if not data.get("articles"):
            return "No news found."

        articles = data["articles"][:3]  # Top 3 articles
        headlines = []
        for article in articles:
            title = article.get("title", "No title available")
            source = article.get("source", {}).get("name", "Unknown source")
            headlines.append(f"{title} from {source}")

        if topic:
            speech_message = f"Here are the latest {topic} news headlines: " + ". ".join(headlines)
        else:
            speech_message = "Here are the top news headlines: " + ". ".join(headlines)

        return speech_message

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
        return "There was a problem fetching news."
    except Exception as err:
        print(f"Error: {err}")
        return "Sorry, I couldn't fetch the news."