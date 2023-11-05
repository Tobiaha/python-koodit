import requests
url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "cadee0da7df217e8df18be22b979347d"
kaupunki = input("Anna kaupunki ")

def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

saa = url + "appid=" + api_key + "&q=" + kaupunki
vastaus = requests.get(saa).json()

kelvin = vastaus['main']['temp']
celsiusaste = kelvin_celsius(kelvin)
print(f"Temperature in {kaupunki}: {celsiusaste:.2f}°C or {kelvin} Kelvin")


