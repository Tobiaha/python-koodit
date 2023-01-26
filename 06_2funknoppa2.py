#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def throw(tahko):
    return random.randint(1, tahko)

tahko = int(input("Montako tahkoa nopassasi on "))
silmaluku = 0
while silmaluku != tahko:
    silmaluku = throw(tahko)
    print(int(silmaluku))
