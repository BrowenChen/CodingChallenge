// GET User Listing.

exports.list = function(req, res, next) {
	req.db.tasks.find({complete:false}).toArray(function(error, tasks){
		if (error) return next(error);
		res.render('tasks', {
			title: 'todo list',
			tasks: tasks || []
		});
	});
};

exports.add = function(req, res, next) {
	if (!req.body || !req.body.name) return next(new Error('No data provided'));
	req.db.tasks.save({
		name: req.body.name,
		completed:false
	}, function(error, task){
		if (error) return next(error);
		console.info('Added task');
		res.redirect('/tasks');
	});
};

exports.del = function(req, res, next) {
	req.db.tasks.removeById(req.task_id, function(error, count){
		if (error) return next(error);
		console.info('Deleted');
		res.send(200);
	});
};
