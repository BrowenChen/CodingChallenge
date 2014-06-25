var express = require('express');
var path = require('path');
var favicon = require('static-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var oauth = require('oauth');
var mongo = require('mongodb');
var gcal = require('google-calendar');
var q = require('q');

var routes = require('./routes/index');
var users = require('./routes/users');

var app = express();

//----------GCAL SETUP
var oa;
var clientId = '549281989393-66n1q1qe2p8hj6ta6r8lqfrrk2u5d17o.apps.googleusercontent.com';
var clientSecret = '12PkXhFB6Txv5-aLalDnLJLC';
var scopes = 'https://www.googleapis.com/auth/calendar';
var googleUserId;
var refreshToken;
var baseUrl;


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(favicon());
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);
app.use('/users', users);

//------ GCAL
app.configure('development',function(){
  console.log('!! DEVELOPMENT MODE !!');

  googleUserId = 'GOOGLE_EMAIL_ADDRESS';
  refreshToken = 'GOOGLE_REFRESH_TOKEN';
  baseUrl = 'DEV_API_URL';
});

app.configure('production', function(){
  console.log('!! PRODUCTION MODE !!');

  googleUserId = 'GOOGLE_EMAIL_ADDRESS';
  refreshToken = 'GOOGLE_REFRESH_TOKEN';
  baseUrl = 'PRODUCTION_API_URL';
});

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
