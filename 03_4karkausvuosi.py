vuosiluku = int(input("kirjoita vuosiluku "))
kv = int(vuosiluku) % 4
kvs = int(vuosiluku) % 100
kvns = int(vuosiluku) % 400

if kvs == 0 and kvns == 0:
    print("Vuosi on karkausvuosi.")
elif kv == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi. ")



