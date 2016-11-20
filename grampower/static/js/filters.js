'use strict';

/* Filters */

angular.module('gramPowerFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});