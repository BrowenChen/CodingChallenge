'use strict'

app.controller('PostsCtrl', function($scope, Post){
	$scope.posts = [];
	$scope.post = {title: '', url: 'https://'};


	$scope.submitPost = function(){
		$scope.posts.push($scope.post);
		$scope.post = {title: '', url: 'https://'};
	}

	$scope.deletePost = function(index){
		$scope.posts.splice(index, 1);
	};


	$scope.firePost = function(){
		Post.save($scope.post, function(ref) {
			$scope.posts[ref.name] = $scope.post
			$scope.post = {title: '', url: 'https://'};

		});
		
	}

	$scope.fireDelete = function(){
		Post.delete({id: postId}, function () {
			delete $scope.posts[postId];
		});
	}


});

