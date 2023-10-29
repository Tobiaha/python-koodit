class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"nimi {self.nimi}")
class Kirja(Julkaisu):
    def __init__(self, kirja, kirjailija, sivumäärä):
        self.kirja = kirja
        self.sivumäärä = sivumäärä
        self.kirjailija = kirjailija
        super().__init__(kirja, kirjailija, sivumäärä)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.kirjoittaja}")
        print(f"{self.sivumäärä}")
        print(f"{self.kirja}")
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi, päätoimittaja)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.päätoimittaja}")
        print(f"{self.nimi}")

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

