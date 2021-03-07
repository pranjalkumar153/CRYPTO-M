var express = require("express");
var app = express();

var parser = require("body-parser");
var nodemailer = require('nodemailer');
var request = require("request");

app.use(parser.urlencoded({ extended: true }));

app.get("/", function(req, res) {
    console.log("WELCOME TO HOMEPAGE!!");
    res.send("WELCOME TO HOMEPAGE!!");
    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'youremail@gmail.com',
            pass: 'yourpassword'
        }
    });

    var mailOptions = {
        from: 'youremail@gmail.com',
        to: 'myfriend@yahoo.com',
        subject: 'Sending Email using Node.js',
        text: 'That was easy!'
    };

    transporter.sendMail(mailOptions, function(error, info) {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
});

app.listen(8000, 8000, function(req, res) {
    console.log("CONNECTED SUCCESSFULLY TO THE SERVER!!");
});