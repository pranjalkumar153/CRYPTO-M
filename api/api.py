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




app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to our Encryption API"

@app.route("/generate_key/<sender>/<receiver>")
def generate_key(sender,receiver):
    return generate_keys(sender,receiver)
  
# registration route functionality
@app.route("/register/<first_name>/<last_name>/<username>/<email>/<password>")
def register(first_name,last_name,username,email,password):
    dictionary_data = {
        "first_name":first_name,
        "last_name":last_name,
        "username":username,
        "email":email,
        "password":password,
        "success" : True
    }
    users = db.child("users").get()
    for x in users.each():
        if(x.val()["email"]==email or x.val()["username"]==username):
            dictionary_data["success"] = False
            break
    if(dictionary_data["success"]==False):
        return dictionary_data
    dictionary_data["success"]
    db.child("users").push(dictionary_data);
    return dictionary_data

# for reference of database functionality

# db.child("name").remove()

# db.child("name").push({"name":"Pranjal Kumar"})
# users = db.child("name").child("name").get()

# print(users)
    
    
app.run(debug=True)