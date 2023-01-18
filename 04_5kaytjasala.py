kayttokerrat = 0
while kayttokerrat <=4:
    kayttaja = input("Anna käyttäjätunnus. ")
    salasana = input("Anna salasana. ")
    if kayttaja == 'python' and salasana == 'rules':
        print("Tervetuloa")
        break
    else:
        print("väärin, kokeile uudestaan.")
        kayttokerrat += 1
else:
    print("Pääsy evätty. ")



