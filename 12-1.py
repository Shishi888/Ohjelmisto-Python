import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print("Vitsin hakeminen epäonnistui.")


hae_chuck_norris_vitsi()
