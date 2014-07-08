angular
    .module('TodoApp', [])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '../static/todo.html',
                controller: 'TodoController'
            })
            .when('/secondPage', {
                templateUrl: '../static/secondPage.html',
                controller: 'SecondController'
            })
            .otherwise({ redirectTo: '/' });
    }])
    .factory('windowAlert', [
        '$window',
        function($window) {
            return $window.alert;
        }
    ])
    .controller('TodoController', [
        '$scope',
        '$http',
        'windowAlert',
        function($scope, $http, windowAlert) {
            $scope.RETRIEVE_DEFAULT_NR = 5;
            $scope.state = {};
            $scope.state.todoList = [];
            $scope.state.retrieveNr = $scope.RETRIEVE_DEFAULT_NR;
            $scope.state.pageName = 'todoList';

//CLASSROOM MODULE FOR DARYL

//NEW EDITING HERE```
            $scope.newgoal = "";
            $scope.goals = [];
            $scope.targetGoal = "";
            $scope.addGoal = function(goal){
	        this.goals.push({
                title: goal,
                done: "Not finished",
                completed: false
                });
            }

            $scope.inProgress = function(target){
                this.targetGoal = target;
                target.done = "In Progress"
                
            }

            $scope.finishGoal = function(target){
                target.done = "Finished";
                target.completed = true;
                

            }

            $scope.resetGoals = function(){
            	alert("Reseting goals");
            	this.goals = [];
            }


//NEW EDITING HERE=            
            $scope.addItem = function() {
                if (!$scope.state.newItem) {
                    windowAlert("why text field must be non-empty");
                } else {
                    $http
                        .post('/todoAdd', {
                            item: $scope.state.newItem
                        })
                        .success(function(data, status, headers, config) {
                            if (data.success) {
                                $scope.retrieveLastNItems(
                                    $scope.state.retrieveNr
                                );
                            } else {
                                windowAlert('Adding of item failed');
                            }
                        })
                        .error(function(data, status, headers, config) {
                        });
                }
            };

            $scope.retrieveLastNItems = function(n) {
                $http
                    .get('/todoRetrieve/' + n)
                    .success(function(data, status, headers, config) {
                        if (data.success) {
                            $scope.state.todoList = data.todoList;
                        } else {
                            windowAlert('Retrieval failed');
                        }
                    })
                    .error(function(data, status, headers, config) {
                        windowAlert("Retrieval failed");
                    });
            };

            $scope.setAndRetrieveLastNItems = function(n) {
                $scope.state.retrieveNr = n;
                $scope.retrieveLastNItems($scope.state.retrieveNr);
            };
        }
    ])
    .directive('navtabs', function() {
        return {
            restrict: 'E',
            replace: true,
            templateUrl: '../static/navtabs.html',
            scope: {
                pageName: '='
            },
            controller: [
                '$scope',
                function($scope) {
                    this.selectTabIfOnPage = function(tab) {
                        if (tab.name === $scope.pageName) {
                            tab.selected = true;
                        }
                    };
                }
            ]
        };
    })
    .directive('tab', function() {
        return {
            require: '^navtabs',
            restrict: 'E',
            replace: true,
            transclude: true,
            scope: {},
            template: '<li ng-class="{ active: selected }"><a href="{{ href }}" ng-transclude></a></li>',
            link: function(scope, element, attr, navtabsCtrl) {
                scope.name = attr.name;
                scope.href = attr.href;
                scope.selected = false;
                navtabsCtrl.selectTabIfOnPage(scope);
            }
        };
    })
    .controller('SecondController', [
        '$scope',
        function($scope) {
            $scope.state = {};
            $scope.state.pageName = 'secondPage';
        }
    ])
    ;

    



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


//CLASSROOM MODULE FOR DARYL


// DUMMY DATA AND TESTING
    $scope.test = function(){
        alert("test");
    };
    $scope.studentOwen = "Owen";  
    $scope.studentCharles = "Charles";  
// DUMMY DATA AND TESTING


    $scope.studentID = "";
    $scope.studentName = "";
    $scope.level = 0;
    $scope.tasks = {};
    $scope.progress = 0;
    $scope.imgUrl = "";

    $scope.addName = function(name){
        this.studentName = name;
    };

    $scope.addTask = function(task){
        this.tasks.push(task);
    };


    $scope.addProgress = function(percent){
        this.progress = percent;
    };

    $scope.addImg = function(img){
        this.imgUrl = img;
    };

};

