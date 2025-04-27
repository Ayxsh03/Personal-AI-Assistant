import requests

def get_joke():
    try:
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url)
        data = response.json()
        if data["type"] == "single":
            return data["joke"]
        else:
            return f"{data['setup']} ... {data['delivery']}"
    except Exception as e:
        print(e)
        return "Couldn't find a joke at the moment."