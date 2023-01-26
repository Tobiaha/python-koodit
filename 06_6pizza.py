#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
#(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pizza(halkaisija1, halkaisija2):
    sade1 = halkaisija1 / 2 / 100
    halkaisija1 = math.pi * (sade1**2)
    sade2 = halkaisija1 / 2 / 100
    halkaisija2 = halkaisija1 = math.pi * (sade2**2)
    return halkaisija1, hinta1, halkaisija2, hinta2


halkaisija1 = int(input("Anna ensimmäisen pitsan halkaisija cm "))
hinta1 = int(input("Ja hinta "))
halkaisija2 = int(input("Anna toisen pitsan halkaisija cm "))
hinta2 = int(input("ja hinta niin pistän sen vertaukseen ensimmäisen pitsan kanssa "))

pizza1 = pizza(halkaisija1, halkaisija2)
arvo1 = halkaisija1 / hinta1
arvo2 = halkaisija2 / hinta2
if arvo1 > arvo2:
    print( "Ensimmäisellä pitsalla on eniten rahallesi vastinetta.", round(arvo1, 2), "m\u00B2/€ " )
else:
    print("Toiseksi valitsemallasi pitsalla on eniten rahallesi vastinetta ",round(arvo2, 2), "m\u00B2/€ ")