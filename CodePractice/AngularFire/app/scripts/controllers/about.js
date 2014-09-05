'use strict';

/**
 * @ngdoc function
 * @name angularFireApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the angularFireApp
 */
angular.module('angularFireApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
