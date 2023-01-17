while True:
    tuuma = int(input("Anna tuuma: "))
    sentti = tuuma * 2.54
    if tuuma < 0:
        break
    print(sentti, "cm")
print("Negatiivinen luku ")