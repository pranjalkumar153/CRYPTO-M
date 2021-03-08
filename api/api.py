from flask import Flask
from flask import jsonify



from api_support import generate_keys

import pyrebase 

config = {
    "apiKey": "AIzaSyCmOhM8JNzT0WHGeaudlFd7pNh37dLt9sI",
    "authDomain": "crypto-m.firebaseapp.com",
    "databaseURL": "https://crypto-m-default-rtdb.firebaseio.com",
    "projectId": "crypto-m",
    "storageBucket": "crypto-m.appspot.com",
    "messagingSenderId": "760957374260",
    "appId": "1:760957374260:web:d549e6c0c55036eac7df61",
    "measurementId": "G-DFR2HEG50W"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("name").remove()

# db.child("name").push({"name":"Pranjal Kumar"})
# users = db.child("name").child("name").get()

# print(users)




app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to our Encryption API"

@app.route("/generate_key/<sender>/<receiver>")
def generate_key(sender,receiver):
    return generate_keys(sender,receiver)
    
# var first_name = req.body.first_name;
#     var last_name = req.body.last_name;
#     var username = req.body.username;
#     var email = req.body.email;
#     var password = req.body.password;
#     var password_confirmation = req.body.password_confirmation;
#     if (password == password_confirmation) {
#         console.log("reg done!!");
#     }    

app.run(debug=True)