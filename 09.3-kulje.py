class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 60
        self.kuljettumatka = 2000

    def kiihdytä(self, muutos):
        self.tämänhetkinennopeus += muutos
        if self.tämänhetkinennopeus >= self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus
        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0

    def kulje(self, tunti):
        self.kuljettumatka += self.tämänhetkinennopeus * tunti

toyota = Auto("ABC-123", 142,)
print(f"Uuden auton rekisteritunnus on {toyota.rekisteritunnus}")
print(f"Huippunopeus on {toyota.huippunopeus} km/h")
print(f"Tämän hetkinen nopeus on {toyota.tämänhetkinennopeus} km/h")

print(f"Auto on kulkenut {toyota.kuljettumatka} km")
toyota.kulje(1.5)
print("Auto jatkaa matkaa...")
print(f"Auto on kulkenut  {toyota.kuljettumatka} km")
