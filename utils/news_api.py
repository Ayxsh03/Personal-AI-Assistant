import requests

API_KEY = "1a9108179d7b47049fd21c6769fcb11c" 

def get_latest_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        response = requests.get(url)
        articles = response.json()["articles"]
        if not articles:
            return "No news found."
        top_headline = articles[0]["title"]
        return f"Top news: {top_headline}"
    except Exception as e:
        print(e)
        return "Failed to fetch news."