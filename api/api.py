from flask import Flask
from flask import jsonify

from api_support import generate_keys, bin_pow

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

# use express-session for authentication


app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to our Encryption API"

@app.route("/generate_key/<sender>/<receiver>")
def generate_key(sender,receiver):
    return generate_keys(sender,receiver)

# login api
@app.route("/login/<username>/<password>")
def login(username,password):
    users = db.child("users").get()
    data_dictionary = {
        "username" : "not assigned",
        "password" : "invalid",
        "correct_credentials": False
    }
    for x in users.each():
        if(x.val()["username"]==username and x.val()["password"]==password):
            data_dictionary["username"] = username
            data_dictionary["password"] = password
            data_dictionary["correct_credentials"] = True
            return data_dictionary
    return data_dictionary

# route for fetching the contacts in database
@app.route("/contacts")
def fetch_contacts():
    users = db.child("users").get()
    contacts_list = []
    for x in users.each():
        data_dictionary = {
            "username" : x.val()["username"],
            "last_name" : x.val()["first_name"],
            "first_name" : x.val()["last_name"] 
        }
        contacts_list.append(data_dictionary)
    contacts = {
        "friends":contacts_list
    }
    return contacts

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
    # hasattr(b, '__iter__')
    if(hasattr(users,'__iter__')==True):
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

# adding route for chat system
# for retrieving the messages
@app.route("/message/<sender>/<receiver>")
def get_messages(sender,receiver):
    messages = db.child("messages").child(sender).child(receiver).get()
    print("From messages")
    print(messages)
    print(type(messages))
    messages_array = []
    if(hasattr(messages,"__iter__")==True):
        for x in messages.each():
            dictionary = dict()
            dictionary[str("message")] = x.val()["message"]
            dictionary[str("response_type")] = x.val()["response_type"]
            messages_array.append(dictionary)
    messages = {"messages" : messages_array,
                "sender" : sender,
                "receiver" : receiver}
    print(messages)
    return messages
    
# route for sending messages
@app.route("/message/send/<sender>/<receiver>/<message>")
def send_messages(sender,receiver,message):
    message_array_encrypted = []
    keys = generate_keys(sender,receiver)
    N = keys["p"]*keys["q"]
    for x in message:
        ascii_val = ord(x)
        c = bin_pow(ascii_val,keys["e"],N)
        message_array_encrypted.append(c)
    message_encrypted = []
    for x in message_array_encrypted:
        message_encrypted.append(str(x))
    db.child("messages").child(sender).child(receiver).push({
        "message" : message_encrypted,
        "response_type" : "sent",
    })
    db.child("messages").child(receiver).child(sender).push({
        "message" : message_encrypted,
        "response_type" : "received",
    })
    return {"message_status":True}
    
    
    
app.run(debug=True)
