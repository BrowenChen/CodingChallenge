'use strict';

/**
 * @ngdoc function
 * @name angularFireApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the angularFireApp
 */
angular.module('angularFireApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });


  angular.module('angularfirebaseApp')
  .controller('MainCtrl', function ($scope, Person) {
    $scope.add = function() {
     var save = Person.$add({
      firstName: $scope.firstName,
      lastName: $scope.lastName
     });

     $scope.firstName = '';
     $scope.lastName = '';

     if(save) {
      alert('saved successfully');
     } else {
      alert('something went wrong');
     }
    });

