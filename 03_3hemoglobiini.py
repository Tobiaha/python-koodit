user_input = input("Anna sukupuolesi, (Mies/Nainen)")
if user_input == 'mies':
  mies = int(input("Anna hemoglobiini arvo (g/l) "))
  if mies > 195:
    print("Hemoglobiini arvo on korkea")
  elif mies < 134:
    print("Hemoglobiini arvo on matala")
  else:
    print("Hemoglobiini arvo on normaali")

if user_input == 'nainen':
  nainen = int(input("Anna hemoglobiini arvo (g/l)"))
  if nainen > 175:
    print("Hemoglobiini arvo on korkea")
  elif nainen < 117:
    print("Hemoglobiini arvo on matala")
  else:
    print("Hemoglobiini arvo on normaali")







