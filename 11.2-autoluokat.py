
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettumatka = 0
    def asetusnopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
    def kulje(self, tunti):
        self.kuljettumatka += self.nopeus * tunti
    def tulosta(self):
        return (f"{self.rekisteritunnus}     |    matka {self.kuljettumatka}  km")
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.akkua_jaljella = akkukapasiteetti
class Polttoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki
        self.bensaa_jaljella = bensatankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5) #rekisterinumero, huippunopeus, akkukapasiteetti
sahkoauto.asetusnopeus(150)
sahkoauto.kulje(3)
print(f"Sähköauton mittari: ", sahkoauto.tulosta())

#print(f"Akkua jäljellä: ", sahkoauto.akkua_jaljella)

polttoauto = Polttoauto("ACD-123", 165, 32.3) #rekisterinumero, huippunopeus, litraa
polttoauto.asetusnopeus(130)
polttoauto.kulje(3)
print(f"Polttomoottoriauton mittari: ", polttoauto.tulosta())

# print(f"Bensaa jäljellä: ", polttoauto.bensaa_jaljella)









