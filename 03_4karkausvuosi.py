vuosiluku = int(input("kirjoita vuosiluku "))
kv = int(vuosiluku) % 4
kvs = int(vuosiluku) % 100

if kv == 0:
    print("Vuosi on karkausvuosi. ")
elif kvs == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi. ")



