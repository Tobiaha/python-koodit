# list.sort(reverse=True)
# lukulista.append(luku)
lukulista = []
while True:

    luku = (input("Anna luku "))

    if luku != '':
        var = int(luku)
        lukulista.append(int(luku))
        continue

    else:
        break
lukulista.sort(reverse=True)
print(lukulista[:5])





