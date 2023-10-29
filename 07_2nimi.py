#Joukko
nimet = set()
nimi = input("Anna tähän nimi ")
while nimi != "":
    if nimi in nimet:
        print(nimi, " on aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print(nimi, " on uusi nimi")
    nimi = input(" Syötä tähän nimi ")

print(nimet)