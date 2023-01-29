#Joukko
nimi = ()
while nimi != "":
    nimet = set()
    nimi = input("Anna tähän nimi ")
    nimet.add(nimi)
    if nimi in nimet:
        print(nimi, " on aiemmin syötetty nimi")
    elif not nimi in nimet:
        print(nimi, " on uusi nimi")

print(nimet)