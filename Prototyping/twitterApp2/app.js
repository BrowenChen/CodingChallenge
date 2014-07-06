// http://www.ibm.com/developerworks/library/wa-nodejs-app/
var port = (process.env.VCAP_APP_PORT || 3000);
var path = require('path');
var express = require('express');
var sentiment = require('sentiment');

//Router
var routes = require('./routes/index');

var app = express();

//View engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html');


//Public setup
app.use(express.static(path.join(__dirname, 'public')));

// app.get('/', function(req, res){
// 	res.send("Hello World");
// });

app.get('/home', function(req, res){
	res.send("Hello World22");
});


app.get('/testSentiment', function(req, res){
	res.render('testSentiment', {title: 'testSentiment'});

	var phrase = req.query.phrase;
	if (!phrase){
		res.send(res);

	} else {
		sentiment(phrase, function(err, result){
			response = 'sentiment(' + phrase + ') ==' + result.score;
			res.send(response);
		});
	}
});

app.listen(port);
console.log("Magic happens at 3000");