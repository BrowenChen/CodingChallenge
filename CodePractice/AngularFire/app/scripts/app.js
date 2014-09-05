'use strict';

/**
 * @ngdoc overview
 * @name angularFireApp
 * @description
 * # angularFireApp
 *
 * Main module of the application.
 */
angular
  .module('angularFireApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });


//Adding firebase into angular. Service Person
  angular
  .module('angularfirebaseApp', [
  'firebase'
  ])

  //Setting the value of the URL to whatever
  .value('fbURL', 'https://angularifictest.firebaseio.com/')
  .factory('Person', function (fbURL, $firebase) {
    return $firebase(new Firebase(fbURL));
  })



