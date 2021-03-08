var express = require("express");
var app = express();

var parser = require("body-parser");
var md5 = require("md5");
var request = require("request");

app.use(parser.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.get(["/", "/homepage", "/sign-in"], function(req, res) {
    res.render("sign-in");
});

app.get("/error", function(req, res) {
    res.render("error");
});

app.post("/register_signup", function(req, res) {
    var first_name = req.body.first_name;
    var last_name = req.body.last_name;
    var username = req.body.username;
    var email = req.body.email;
    var password = req.body.password;
    var password_confirmation = req.body.password_confirmation;
    if (password == password_confirmation) {
        // add the api implementation here
        // "/register/<first_name>/<last_name>/<email>/<password>"
        request("/", function(error, response, body) {
            if (!error && response.statusCode == 200) {
                results = JSON.parse(body);
                console.log(results.Search);
                console.log(typeof(Object.values(results.Search)));
                //Converted the object to array;
                results = Object.values(results.Search);
                console.log(results);
                console.log("INFORMATION SUCCESFULLY FETCHED");
            } else {
                console.log("AN ERROR OCCURRED WHILE CONNECTING TO THE SERVER!!");
            }
        });
    } else {
        app.redirect("/error");
    }
});

app.get("/sign-up", function(req, res) {
    res.render("sign-up");
});

app.get("/contacts", function(req, res) {
    res.render("contacts");
});

app.get("/message", function(req, res) {
    res.render("message");
});

app.listen(8000, 8000, function(req, res) {
    console.log("CONNECTED SUCCESSFULLY TO THE SERVER!!");
});