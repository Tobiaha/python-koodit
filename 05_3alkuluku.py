kokonaisluku = int(input("Anna kokonaisluku niin kerron sinulle onko se alkuluku "))

if kokonaisluku == 1:
    print(kokonaisluku, "ei ole alkuluku")
elif kokonaisluku > 1:
    for i in range(2, kokonaisluku):
        if (kokonaisluku % i) == 0:
            print(kokonaisluku, "Ei ole alkuluku ")
            break
    else:
        print(kokonaisluku, "On alkuluku")
else:
    print(kokonaisluku, "Ei ole alkuluku")


