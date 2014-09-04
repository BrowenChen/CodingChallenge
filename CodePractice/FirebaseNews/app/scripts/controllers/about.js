'use strict';

/**
 * @ngdoc function
 * @name fireBaseAngularAppApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the fireBaseAngularAppApp
 */
angular.module('fireBaseAngularAppApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma',
      'Another'
    ];
  });
