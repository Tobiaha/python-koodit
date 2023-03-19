class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros == self.alin:
            print("Olet alimmassa kerroksessa")

    def kerros_ylös(self):
        self.kerros += 1
        if self.kerros == self.ylin:
            print("Hissi on ylimmässä kerroksessa")
            self.kerros = self.ylin

    def siirry_kerrokseen(self, kerros):
        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerros_ylös()
                print(f"Olet kerroksessa {self.kerros}")
            elif self.kerros > kerros:
                self.kerros_alas()
                print(f"Olet kerroksessa {self.kerros}")


h = Hissi(1, 10)
h.siirry_kerrokseen(10)
print(h.kerros)