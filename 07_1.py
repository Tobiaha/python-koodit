# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kkn = int(input("Kirjoita kuukauden numero (1-12): "))
if kkn >= 3 and kkn <= 5:
    print(vuodenajat[0])
elif kkn >= 6 and kkn <= 8:
    print(vuodenajat[1])
elif kkn >= 9 and kkn <= 11:
    print(vuodenajat[2])
elif kkn == 12 or kkn == 1 or kkn == 2:
    print(vuodenajat[3])
