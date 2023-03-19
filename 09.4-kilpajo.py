import random
class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0
    def kiihdytä(self, muutos):
        self.tämänhetkinennopeus += muutos
        if self.tämänhetkinennopeus >= self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus
        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0

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
    for auto in autot:
        random.randint(-10, 15)  # km/h
        auto.kulje(1)
        print(f"{auto.kuljettumatka} km")
    if auto.kuljettumatka <= 10000:
        kilpailu = False
        break
print(f"rekisteri, huippunopeus, nopeus, matka")
for auto in autot:
    auto.ominaisuudet()


