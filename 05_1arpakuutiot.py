import random
nopat = int(input("montako arpakuutioita heitetään? "))
summaluvut = []
for d in range(nopat):
    noppaheitot = random.randint(1, 6)
    summaluvut.append(noppaheitot)
print(summaluvut)
print("Heitettyjen noppien summa on: ", sum(summaluvut))

