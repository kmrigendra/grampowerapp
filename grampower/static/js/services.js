'use strict';

/* Services */

angular.module('customServices', [])
	.factory('localResource', function() {
		return {
            joinList: function(arrayItem) {
            	var newArray = []; 
                arrayItem.forEach(function (item){ 
		    		if(item.status){ 
		    			newArray.push(item.name);
		    		}
		    	});
		    	return newArray;
            }
        };
	})
;
