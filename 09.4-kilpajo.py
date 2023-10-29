import random
class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0
    def kiihdytä(self, muutos):
        self.tämänhetkinennopeus += muutos
    def kulje(self, tunti):
        self.kuljettumatka += self.tämänhetkinennopeus * tunti

    def ominaisuudet(self):
        print(self.rekisteritunnus)
        print(self.huippunopeus)
        print(self.tämänhetkinennopeus)
        print(self.kuljettumatka)

autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    auto = Auto(rekisteritunnus)
    autot.append(auto)


kilpailu = True

while kilpailu:
    for i in autot:
        auto.kiihdytä(random.randint(-10, 15))  # km/h
        auto.kulje(1)                           #tunti

        print(f"{auto.rekisteritunnus} on kulkenut {auto.kuljettumatka} km")

        if auto.kuljettumatka >= 10000:
          kilpailu = False
          break


print(autot)


