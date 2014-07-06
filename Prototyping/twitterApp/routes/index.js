var express = require('express');
var router = express.Router();
var sentiment = require('sentiment');
var twitter = require('ntwitter');

var tweeter = new twitter({
	consumer_key: '4xjZsNlxIIO1Mub7LMaAopSPi',
	consumer_secret: 'xfPrAKyEruv6oett5dq2GAFFzE97AmF8KZOXJcWerGxZMpjhdI',
	access_token_key: '735299959-HTczY5d6FmyAr5zdFZSertC3vMpIPdIWMtI8XKF1',
	access_token_secret:'q0gLrlgozv6RobEVepIIjcaFBzgeA9v0uByABqDKurKSc'
});

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

/* GET home page */
router.get('/home', function(req, res){
	res.render('index', {title: 'Home'});
});

/* twitterCheck*/
router.get('/testCheck', function(req, res){
	tweeter.verifyCredentials(function (err, data){
		res.send("Hello " + data.name + ". I am in your twitters.");
	});
});


/* GET TestSentiment */
router.get('/testSentiment', function(req, res){
	var response=  "<HEAD>" +
          "<title>Twitter Sentiment Analysis</title>\n" +
          "</HEAD>\n" +
          "<BODY>\n" +
          "<P>\n" +
          "Welcome to the Twitter Sentiment Analysis app.  " +   
          "What phrase would you like to analzye?\n" +                
          "</P>\n" +
          "<FORM action=\"/testSentiment\" method=\"get\">\n" +
          "<P>\n" +
          "Enter a phrase to evaluate: <INPUT type=\"text\" name=\"phrase\"><BR>\n" +
          "<INPUT type=\"submit\" value=\"Send\">\n" +
          "</P>\n" +
          "</FORM>\n" +
          "</BODY>";
    var phrase = req.query.phrase;
    if (!phrase) {
        res.send(response);
    } else {
        sentiment(phrase, function (err, result) {
            response = 'sentiment(' + phrase + ') === ' + result.score;
            res.send(response);
        });
    }

});


router.get('/watchTwitter', function(req, res){
	var stream;
	var testTweetCount = 0;
	var phrase = 'biber';

	tweeter.verifyCredentials(function(err, data){
		if (err){
			res.send("Error connectiong" + err);
		}

		stream = tweeter.stream('statuses/filter',{
			'track': phrase
		}, function(stream){
			res.send("Monitoring Twitter for " + phrase + " logging Twitter traffic");
			stream.on('data', function(data){
				testTweetCount++;
				if (testTweetCount % 50 === 0){
					console.log("Tweet #" + testTweetCount + ": " + data.text);
				}
			});

		});
	});
});

module.exports = router;
