var express = require("express");
var app = express();

var parser = require("body-parser");

var request = require("request");

app.use(parser.urlencoded({ extended: true }));

app.set("view engine", "ejs");

app.get("/", function(req, res) {
    res.render("sign-in.ejs");
});
app.get("/signin", function(req, res) {
    res.render("sign-in.ejs");
});
app.get("/signup", function(req, res) {
    res.render("sign-up.ejs");
});


app.listen(8000, 8000, function(req, res) {
    console.log("CONNECTED SUCCESSFULLY TO THE SERVER!!");
});