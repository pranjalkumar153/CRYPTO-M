var express = require("express");
var app = express();

var parser = require("body-parser");

var request = require("request");

app.use(parser.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.get(["/", "/homepage", "/sign-in"], function(req, res) {
    res.render("sign-in");
});

app.post("/register_signup", function(req, res) {
    var first_name = req.body.first_name;
    var last_name = req.body.last_name;
    var username = req.body.username;
    var email = req.body.email;
    var password = req.body.password;
    var password_confirmation = req.body.password_confirmation;
    if (password == password_confirmation) {
        console.log("reg done!!");
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