user_input = input("Minkä hyttiluokan olet varannut? (LUX, A, B, C) ")

if user_input.capitalize() == 'LUX':
    print("LUX on parvekkeellinen hytti yläkannella.")
elif user_input.capitalize() == 'A':
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_input.capitalize() == 'B':
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_input.capitalize() == 'C':
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
