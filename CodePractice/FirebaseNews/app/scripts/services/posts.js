app.factory('Post', function($resource) {
	return $resource('https://brilliant-heat-898.firebaseio.com/posts/:id.json');
})