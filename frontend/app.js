var express = require("express");
var app = express();

var parser = require("body-parser");
var nodemailer = require('nodemailer');
var request = require("request");

app.use(parser.urlencoded({ extended: true }));


app.listen(8000, 8000, function(req, res) {
    console.log("CONNECTED SUCCESSFULLY TO THE SERVER!!");
});