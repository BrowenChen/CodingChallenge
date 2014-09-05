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



  angular
  .module('angularfirebaseApp', [


  'firebase'

  
  ])
  .value('fbURL', 'https://angularifictest.firebaseio.com/')
  .factory('Person', function (fbURL, $firebase) {
    return $firebase(new Firebase(fbURL));
  })

