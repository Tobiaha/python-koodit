import requests

pyynto = "https://api.chucknorris.io/jokes/random/"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        vitsi = json_vastaus["value"]
        print(vitsi)
except requests.exceptions.RequestException as e:
    print("Jotain meni pieleen.")

