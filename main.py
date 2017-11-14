from flask import Flask, request, url_for
import matlab.engine
from flask_cors import CORS
import json

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



app.run(debug=False)
