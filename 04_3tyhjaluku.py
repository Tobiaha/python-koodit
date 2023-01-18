number_array = []
while True:
     number =  (input("Anna luku: "))

     if number != "":
          try:
               var = int(number)
               number_array.append(int(number))
               continue
          except ValueError:
               print("Ei ole numero")
          print(min), max

     else:
          break
print(min(number_array), max(number_array))




