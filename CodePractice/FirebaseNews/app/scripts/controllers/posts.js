'use strict'

app.controller('PostsCtrl', function($scope){
	$scope.posts = [];
	$scope.post = {title: '', url: 'https://'};


	$scope.submitPost = function(){
		$scope.posts.push($scope.post);
		$scope.post = {title: '', url: 'https://'};
	}



});