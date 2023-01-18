import random
arvonta = random.randint(1, 10)
player = int(input("Arvaa luku 1-10 "))

while player != arvonta:
    player = int(input("Arvaa luku 1-10 "))
    if player < arvonta:
        print("Liian pieni arvaus ")
    elif player > arvonta:
        print("Liian suuri arvaus ")
    elif player == arvonta:
        print("Oikein ")


