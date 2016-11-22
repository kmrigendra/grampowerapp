'use strict';

angular.module('GramPower', ['customServices', 'customDirectives', 'ngRoute','ngMap','ngImgCrop'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/index.html',
			controller: IndexController
		})
		.when('/store', {
			templateUrl: 'static/partials/store.html',
			controller: StoreController
		})
		.when('/register', {
			templateUrl: 'static/partials/register.html',
			controller: RegisterController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
;