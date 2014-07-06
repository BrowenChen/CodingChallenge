var graph = require('fbgraph');



exports.getFacebook = function(req, res, next){
  var token = _.find(req.user.tokens, { kind: 'facebook' }); //Database 
  graph.setAccessToken(token.accessToken);

   async.parallel({
    getMe: function(done) {
      graph.get(req.user.facebook, function(err, me) {
        done(err, me);
      });
    },
    getMyFriends: function(done) {
      graph.get(req.user.facebook + '/friends', function(err, friends) {
        done(err, friends.data);
      });
    }
  },
  function(err, results) {
    if (err) return next(err);
    res.render('api/facebook', {
      title: 'Facebook API',
      me: results.getMe,
      friends: results.getMyFriends,

      //Insert parameters here to pass into the jade file ------
      photos: data
      
    });
  });
};

