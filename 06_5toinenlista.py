def sumnum(luvut, n=0):
    if n == len(luvut):
        exit()
    if luvut[n] % 2 == 0:
        print(luvut[n])
    sumnum(luvut, n+1)

luvut2 = [1, 2, 3, 4, 5, 6, 17, 10]
luvut1 = [1, 2, 3, 4, 5, 6, 17, 10]

print("Tässä alkuperäiset numerot listasta ")
print(luvut2)
print("Ja tässä tasalukuiset numerot listasta ")
sumnum(luvut1)



