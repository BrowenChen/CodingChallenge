var express = require('express');
var router = express.Router();


router.get('/test', function(req, res){
	res.render('testSentiment', {title: 'test'});
});

router.get('/', function(req, res){
	res.send("Hseee");
})

module.exports = router;