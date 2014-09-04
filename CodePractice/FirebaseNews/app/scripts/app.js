'use strict';

/**
 * @ngdoc overview
 * @name fireBaseAngularAppApp
 * @description
 * # fireBaseAngularAppApp
 *
 * Main module of the application.
 */
var app = angular
  .module('fireBaseAngularAppApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])


  app.config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/posts.html',
        controller: 'PostsCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
