from flask import Flask
from flask import jsonify

from api_support import generate_keys

app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to our Encryption API"

@app.route("/generate_key/<sender>/<receiver>")
def generate_key(sender,receiver):
    return generate_keys(sender,receiver)

app.run(debug=True)