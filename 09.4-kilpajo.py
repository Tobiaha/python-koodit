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
    def rivi(self):
        print(f"{self.rekisteritunnus}      |       {self.huippunopeus}       |       {self.kuljettumatka}")
    def rivi10(self):
        print(f"{self.rekisteritunnus}     |       {self.huippunopeus}       |       {self.kuljettumatka}")


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    auto = Auto(rekisteritunnus)
    autot.append(auto)
    #print(auto, rekisteritunnus)


kilpailu = True

while kilpailu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))  # km/h
        auto.kulje(1)                           #tunti

        if auto.kuljettumatka >= 10000:
          kilpailu = False
          break
def tee_taulukko(lista):

    print("Rekisterinumero  huippunopeus  kuljettu matka")

    i = 0
    for auto in lista:
        i += 1
        if i < 10:
            auto.rivi()
        else:
            auto.rivi10()


tee_taulukko(autot)




