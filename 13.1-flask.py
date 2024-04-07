from flask import Flask, request, Response
import json

app = Flask(__name__)

def prime_numb(kokonaisluku):
    if kokonaisluku == 1:
        return False
    elif kokonaisluku > 1:
        for i in range(2, kokonaisluku):
            if (kokonaisluku % i) == 0:
                return False
        else:
            return True
    else:
        return False

    return num
def calc_sum(a, b):
    return a + b

def multiply(a, b):
    return a * b
@app.route('/alkuluku/<luku>')
def calculate(luku):
  #  print(request.args)
  #try:
        result = prime_numb(int(luku)) #ottaa def alkuluvusta kyllä/ei True or False
        #oletuksena dictionary muuttuu automaattisesti jsoniksi
        #statuksella 200 (ok)
        response_body = json.dumps(
            {"Number": luku, "isPrime": result }
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