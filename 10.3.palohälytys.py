class Hissi:
    def __init__(self, alin_kerros, ylimmän_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmän_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa!")

class Talo:
    def __init__(self, alin_kerros, ylimmän_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimmän_kerros
        self.hissit = []
        for i in range(hissien_lukumäärä):
            self.hissit.append(Hissi(alin_kerros, ylimmän_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            print("PALOHÄLYTYS")
            hissi.siirry_kerrokseen(self.alin_kerros)

talo = Talo(1, 10, 2)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.palohälytys()