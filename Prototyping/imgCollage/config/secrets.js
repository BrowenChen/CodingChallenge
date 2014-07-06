var _ = require('lodash');
var passport = require('passport');

var FacebookStrategy = require('passport-facebook').Strategy;
var User = require('../models/User');
var secrets = require('./secrets');


passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  User.findById(id, function(err, user) {
    done(err, user);
  });
});
