var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/index', function(req, res) {
  res.render('index', { title: 'Express' });
});

// frontend routes =========================================================
// route to handle all angular requests
router.get('*', function(req, res) {
	res.sendfile('./public/views/index.html'); // load our public/index.html file
});
module.exports = router;
