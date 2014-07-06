var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Todo App' });
});

router.get('/tasks', function(req, res){
	res.render('tasks', {title: 'tasks'});
});

module.exports = router;
