'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	$scope.title = "about";
	$scope.sayHi = function(){
		
	}
}

function PostListController($scope, Post) {
	var postsQuery = Post.get({}, function(posts) {
		$scope.posts = posts.objects;
	});
}

function PostDetailController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}

/* Custom controllers */

function TaskController($scope){
	$scope.title = "Tasks";
}


//Student 
function StudentController($scope){

  $scope.studentDescription = "Owen";
  $scope.action = "None Set";
  $scope.studentNumber = 0;
  $scope.rightNumber = 0;
  $scope.wrongNumber = 0;

  $scope.studentList = []; 


  $scope.addRightCount = function(){
    this.rightNumber++;
  };

  $scope.addWrongCount = function(){
    this.wrongNumber++;
  };

  $scope.addStudent = function(student){
    this.studentList.push(student);
  };


  $scope.removeAllStudents = function(){
    this.studentList = [];
  }

  $scope.studentOwen = {
    name: "Owen",
    status: {rightNumber: 0, 
             wrongNumber: 0}
  };  
};

function GoalsController($scope){
  $scope.title = "Your goals Here"
}
