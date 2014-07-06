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
// var everyauth = require('everyauth');



var routes = require('./routes/index');
var users = require('./routes/users');

// var app = express();
// app
//   .use(express.bodyParser())
//   .use(express.cookieParser('mr ripley'))
//   .use(express.session())
//   .use(everyauth.middleware(app));


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





// var everyauth = require('everyauth')
//   , connect = require('connect');

// everyauth.google
//   .appId('549281989393-ok3m5pg3qrcklpro21n1l37utq94om2q.apps.googleusercontent.com')
//   .appSecret('3wdgJkC3CgRvaVbbjqw-rFPp')
//   .scope('https://www.google.com/m8/feeds') // What you want access to
//   .handleAuthCallbackError( function (req, res) {
//     // If a user denies your app, Google will redirect the user to
//     // /auth/facebook/callback?error=access_denied
//     // This configurable route handler defines how you want to respond to
//     // that.
//     // If you do not configure this, everyauth renders a default fallback
//     // view notifying the user that their authentication failed and why.
//   })
//   .findOrCreateUser( function (session, accessToken, accessTokenExtra, googleUserMetadata) {
//     // find or create user logic goes here
//     // Return a user or Promise that promises a user
//     // Promises are created via
//     //     var promise = this.Promise();
//   })
//   .redirectPath('/');

// var routes = function (app) {
//   // Define your routes here
// };

// connect(
//     connect.bodyParser()
//   , connect.cookieParser()
//   , connect.session({secret: 'whodunnit'})
//   , everyauth.middleware()
//   , connect.router(routes);
// ).listen(3000);
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
