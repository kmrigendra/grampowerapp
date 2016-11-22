'use strict';

/* Filters */

angular.module('customFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});

