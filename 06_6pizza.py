#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
#(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pizza(halkaisija, hinta):
    sade = (halkaisija / 2) / 100 #säde
    area = math.pi * (sade**2) #pinta-ala
    arvo =  hinta / area      #arvo neliömetreinä
    return arvo


halkaisija1 = int(input("Anna ensimmäisen pitsan halkaisija cm "))
hinta1 = int(input("Ja hinta "))
halkaisija2 = int(input("Anna toisen pitsan halkaisija cm "))
hinta2 = int(input("ja hinta niin pistän sen vertaukseen ensimmäisen pitsan kanssa "))

pizza1 = pizza(halkaisija1, hinta1)
pizza2 = pizza(halkaisija2, hinta2)

if pizza1 > pizza2:
    print("Ensimmäisellä pitsalla on eniten rahallesi vastinetta.")
else:
    print("Toiseksi valitsemallasi pitsalla on eniten rahallesi vastinetta ")