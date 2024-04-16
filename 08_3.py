
import mysql.connector
from geopy.distance import geodesic as GD


def request(a):
    kursori = yhteys.cursor()
    kursori.execute(a)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='',
    autocommit=True
)

ident = input("Sijaitse ensimmäinen lentokoneaseman koodi: "), input("Sijaitse toinen letokoneaseman koodi: ")
result = list()
for item in ident:
       result.append(request("SELECT latitude_deg, longitude_deg from airport where ident like '"+str(item)+"';"))
print(f"{GD(result[0][0],result[1][0]).km} km")
