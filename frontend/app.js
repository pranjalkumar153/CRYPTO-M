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

app.get("/404_page", function(req, res) {
    res.render("page_404");
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
        var url = "http://127.0.0.1:5000/register";
        url += "/" + first_name;
        url += "/" + last_name;
        url += "/" + username;
        url += "/" + email;
        url += "/" + md5(password);
        // add the api implementation here
        // "/register/<first_name>/<last_name>/<username>/<email>/<password>"
        request(url, function(error, response, body) {
            if (!error && response.statusCode == 200) {
                results = JSON.parse(body);
                console.log(results);
                console.log("INFORMATION SUCCESFULLY FETCHED");
            } else {
                console.log("AN ERROR OCCURRED WHILE CONNECTING TO THE SERVER!!");
                app.redirect("/404_page");
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