class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, muutos):
        self.tämänhetkinennopeus += muutos
        if self.tämänhetkinennopeus >= self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus
        if self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0







toyota = Auto("ABC-123", 142, )
print(f"Uuden auton rekisteritunnus on {toyota.rekisteritunnus}")
print(f"Huippunopeus on {toyota.huippunopeus} km/h")



print("Toyota kiihdyttää...")
toyota.kiihdytä(+30)
toyota.kiihdytä(+70)
toyota.kiihdytä(+50)
print(f"Tämän hetkinen nopeus {toyota.tämänhetkinennopeus} km/h")
toyota.kiihdytä(-200)
print(f"Hätäjarrutus...nopeus nyt {toyota.tämänhetkinennopeus} km/h")
print(f"Kuljettu matka {toyota.kuljettumatka}")


