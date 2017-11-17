from flask import Flask, request, url_for
import matlab.engine
from flask_cors import CORS
import json
import numpy as np
from random import randint

app = Flask(__name__)
CORS(app)
eng = matlab.engine.start_matlab()

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/triArea/<base>/<altura>')
def triArea(base, altura):
    b = int(base)
    a = int(altura)
    ret = eng.triarea(float(base), float(altura))
    return str(ret)


@app.route('/complex_test', methods=['POST'])
def complex_test():
    j = request.get_json()
    a1 = randint(0, 9)
    a2 = randint(0, 9)
    a3 = randint(0, 9)
    a4 = randint(0, 9)
    entrada = matlab.double([[a1,a2], [a3,a4]])
    saida = eng.invmatrix(entrada)
    resposta = ''

    resposta += 'Matriz de entrada:\n'
    for line in entrada:
        resposta += str(line)
        resposta += '\n'

    resposta += 'Matriz de saida:\n'
    for line in saida:
        resposta += str(line)
        resposta += '\n'

    
    return resposta


app.run(debug=False)
