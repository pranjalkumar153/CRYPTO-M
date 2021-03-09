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

# db.child("name").remove()

# db.child("name").push({"name":"Pranjal Kumar"})
# users = db.child("name").child("name").get()

# print(users)

data = db.child("id").get()
print(data.key())
    
