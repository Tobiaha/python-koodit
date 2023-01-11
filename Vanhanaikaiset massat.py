
leiviskat = float(input(" Anna leiviskät"))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

leiviskat = (20 * 32 * 13.3 * leiviskat)

naulat = (32 * 13.3 * naulat)

luodit = (13.3 * luodit)


paino = (leiviskat + naulat + luodit)

print(paino / 1000, "kg")
round(paino % 1000, 2)
