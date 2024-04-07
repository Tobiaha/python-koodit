import mysql.connector
from flask import Flask, request, Response
import json

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='must4t9kk1',
    autocommit=True)
app = Flask(__name__)

@app.route('/kenttä/<icao>')
def lentokentta(icao):
    sql = "select name, municipality from airport where ident = '" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    kursori.close()

    if len(tulos) == 0:
        return Response(response=json.dumps({"message": "airfield not found"}), status=404, mimetype="application/json");
    else:
        response_body = json.dumps(
            {"ICAO": icao, "Name": tulos[0][0], "Municipality": tulos[0][1]}
        )
        return Response(response=response_body, status=200, mimetype="application/json")





@app.errorhandler(404)
def page_not_found(error):
    print(error)
    response_body = json.dumps(
        {"error": error.name, "description": error.description, "status": error.code}
    )
    return Response(
        response=response_body,
        status=error.code,
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run(use_reloader=True, host='localhost', port=3000)