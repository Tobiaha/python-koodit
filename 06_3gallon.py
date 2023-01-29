
def bensa(gallon):
     return float(gallon) * 3.785
litra = 0
gallon = float(input("Anna gallonamäärä niin muutan sen litroiksi "))
while gallon > 0:
    litra = bensa(gallon)
    print(float(litra), "Litraa")
    gallon = float(input("Anna gallonamäärä niin muutan sen litroiksi "))






