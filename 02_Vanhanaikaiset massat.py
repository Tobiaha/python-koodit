
leiviskat = float(input(" Anna leiviskät"))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

leiviskat = (20 * 32 * 13.3 * leiviskat)

naulat = (32 * 13.3 * naulat)

luodit = (13.3 * luodit)


paino = float((leiviskat + naulat + luodit))
print(round(paino / 1000))
print("kilogrammaa ja ")
print(round(paino % 1000))
print("grammaa.")





