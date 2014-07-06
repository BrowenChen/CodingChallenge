var express = require('express');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var cheerio = require('cheerio'); //jQuery for server side
var request = require('request');
var fs = require('fs');


var routes = require('./routes/index');
var users = require('./routes/users');

var app = express();

//REST
app.get('/scrape', function(req, res){

    url = 'http://www.imdb.com/title/tt1229340/';
    console.log("looking into url " + url);
    request(url, function(err, response, html){
        if (err){
            console.log("EEEROR");
        }
        if (!err){
            var $ = cheerio.load(html)

            var title, release, rating;
            var json = {title: "", release: "", rating: ""};

            $('.header').filter(function(){
                var data = $(this);

                title = data.children().first().text();
                release = data.children().last().children().text();

                json.title = title;
                json.release = release;
            })


            $('.star-box giga-star').filter(function(){
                var data = $(this);

                rating = data.text();
                json.rating = rating;
            })
        }



        // To write to the system we will use the built in 'fs' library.
        // In this example we will pass 3 parameters to the writeFile function
        // Parameter 1 :  output.json - this is what the created filename will be called
        // Parameter 2 :  JSON.stringify(json, null, 4) - the data to write, here we do an extra step by calling JSON.stringify to make our JSON easier to read
        // Parameter 3 :  callback function - a callback function to let us know the status of our function

        fs.writeFile('out.json', JSON.stringify(json, null, 4), function(err){
            console.log("File successfully writtent");
        })

        //Message to check console.
        res.send("Check your files");
    });


});

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(favicon());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
app.use('/users', users);

/// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

/// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});


module.exports = app;
