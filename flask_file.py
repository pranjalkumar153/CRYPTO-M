from flask import Flask, render_template
# render_template function is used to render templates 
# in html format via routes present in templates folder
app = Flask(__name__)
app.config['SECRET_KEY']="04e10d2979e7f54c77f0f2205fb10f2f029ee51b0ddefaec978c455376028a19"
posts = [
    {"name": "Pranjal Kumar",
     "content": "Had a nice day today!!",
     "date": "26-Jan-2021"},
    {"name": "Abhisekh Sahai",
     "content": "LOL!! Legends seedha khoon peete hain!",
     "date": "31-Jan-2021"},
]

@app.route("/")
@app.route("/login") 
@app.route("/signup")#multiple routes to same page
def hello():
    return render_template("login_signup.html")
    # the data will be accessible by html by the name posts

# @app.route("/about")
# def about():
#     return render_template("about.html")

if __name__=="__main__":
    app.run(debug = True)
    # the parameter debug when set to true loads the changes made to the page automatically