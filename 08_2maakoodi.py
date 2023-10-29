def lentokentta(ident):
    sql = "select name, municipality from airport where ident = '" + ident + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
#main
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='must4t9kk1',
    autocommit=True
)
