import requests

def hae_saa(paikkakunta, api_avain):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&lang=fi&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lampotila = data["main"]["temp"]
        kuvaus = data["weather"][0]["description"]
        print(f"Sää kohteessa {paikkakunta}: {kuvaus}, lämpötila: {lampotila} °C")
    else:
        print("Sään hakeminen epäonnistui. Tarkista paikkakunta ja API-avain.")


api_avain = "OMA_API_AVAIN"
paikkakunta = input("Anna paikkakunnan nimi: ")
hae_saa(paikkakunta, api_avain)