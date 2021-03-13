var express = require("express");
var app = express();

var parser = require("body-parser");
var md5 = require("md5");
var request = require("request");
var session = require("express-session");

app.use(express.urlencoded({ extended: true }));
app.use(session({ secret: "43d5a9ff7e1f25311e0703f3fea42f6f62673f1cd6171a3834188fad990d4c22" }));



app.use(parser.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.get(["/", "/homepage", "/sign-in", "/login"], function(req, res) {
    if (req.session.username && req.session.password) {
        res.redirect("/message");
    } else {
        res.render("sign-in");
    }
});

app.post("/login", function(req, res) {
    if (req.session.username && req.session.password) {
        res.redirect("/contacts");
    }
    username = req.body.username;
    password = md5(req.body.password);
    url = "http://127.0.0.1:5000/login";
    url += "/" + username;
    url += "/" + password;
    request(url, function(error, response, body) {
        if (!error && response.statusCode == 200) {
            credentials = JSON.parse(body);
            console.log("from login: ");
            console.log(credentials);
            if (credentials.correct_credentials == true) {
                req.session.username = credentials.username;
                req.session.password = credentials.password;
                res.redirect("/contacts");
            } else {
                res.redirect("/");
            }

        } else {
            console.log("CAN'T LOAD PAGE!! REFRESH AND TRY AGAIN!!");
        }
    });
});

app.get("/404_page", function(req, res) {
    res.render("page_404");
});

app.get("/error", function(req, res) {
    res.render("error");
});

app.get("/already_exists", function(req, res) {
    res.render("already_exists");
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
                if (results.success == true) {
                    res.redirect("/success");
                } else {
                    res.redirect("/already_exists");
                }
            } else {
                console.log("AN ERROR OCCURRED WHILE CONNECTING TO THE SERVER!!");
                res.redirect("/404_page");
            }
        });
    } else {
        res.redirect("/error");
    }
});

app.get("/success", function(req, res) {
    res.render("success", { user: results });
});

app.get("/sign-up", function(req, res) {
    res.render("sign-up");
});

var contacts = "";

app.get("/contacts", function(req, res) {
    if (req.session.username && req.session.password) {
        url = "http://127.0.0.1:5000/contacts";
        request(url, function(error, response, body) {
            if (!error && response.statusCode == 200) {
                contact_list = JSON.parse(body.friends);
                console.log(contact_list);
                contacts = contact_list.friends;
                res.redirect("/users", { contacts: contact_list });
            } else {
                res.redirect("/404_page");
            }
        });
    } else {
        res.send("<h1>You need to login to view this page.</h1>");
    }
});

app.get("/users", function(req, res) {
    if (req.session.username && req.session.password) {
        res.render("contacts", { contacts: contact_list });
    } else {
        res.send("<h1>You need to login to view this page.</h1>");
    }

});


app.get("/message", function(req, res) {
    if (req.session.username && req.session.password) {
        res.render("message");
    } else {
        res.send("You need to login in order to view this page!!");
    }
});

app.listen(8000, 8000, function(req, res) {
    console.log("CONNECTED SUCCESSFULLY TO THE SERVER!!");
});


// sorting out the signup system