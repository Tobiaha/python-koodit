class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

toyota = Auto("ABC-123", 142)
print(f"Uuden auton rekisteritunnus on {toyota.rekisteritunnus}")
print(f"Huippunopeus on {toyota.huippunopeus} km/h")
print("Tämän hetkinen nopeus {toyota.tämänhetkinennopeus}")
print("Kuljettu matka {toyota.kuljettumatka}")
