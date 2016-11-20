'use strict';

/* Controllers */

function IndexController($scope, $http, $location) {
 	$http.get('/stores-all?page=0').success(function(response) {
    	$scope.store = response.data;
  	});
  	$scope.StoreClicked = function(idxVal){
        $location.path('/store/').search({id: idxVal});
  	};
}

function StoreController($scope, $http, $location) {
	var queryString = $location.search();
	$http.get('/get-store?id='+queryString.id).success(function(response) {
    	$scope.store = response.data;
  	});	
}

function RegisterController($scope, $location, $http) {
	$scope.currentImage = '';
 	$scope.store = {
		name: '',
		licence_no: '',
		country: 'India',
		street_address: '',
		postal_code: '',
		city: '',
		contact_number: '',
		description: '',
		working_days:[{
			name: 'Monday',
			status: true,
		},{
			name: 'Tuesday',
			status: false,
		},{
			name: 'Wednesday',
			status: false,
		},{
			name: 'Thursday',
			status: false,
		},{
			name: 'Friday',
			status: false,
		},{
			name: 'Saturday',
			status: false,
		},{
			name: 'Sunday',
			status: false,
		}],
		cover_image: '',
		thumbnails: [],
		pro_categories: [{
			name: 'Mobile & Accessories',
			id: 0,
			status: false,
		},{
			name: 'Electronics',
			id: 1,
			status: false,
		},{
			name: 'Home & Kitchen',
			id: 2,
			status: false,
		},{
			name: 'Sports, Fitness & Hobbies',
			id: 3,
			status: false,
		},{
			name: 'Cars & Bikes',
			id: 4,
			status: false,
		},{
			name: 'Musical Instruments',
			id: 5,
			status: false,
		},{
			name: 'Books, Music & Movies',
			id: 6,
			status: false,
		},{
			name: 'Stationery',
			id: 7,
			status: false,
		},{
			name: 'Industrial Supplies',
			id: 8,
			status: false,
		},{
			name: 'Others',
			id: 9,
			status: true,
		},],
		latitude: '',
		longitude: '', 
	};
 

	$scope.addToThumbnail = function(){
		$scope.store.thumbnails.push($scope.currentImage);
		$scope.currentImage = '';
	};

	$scope.removeThumbnail = function(idxVal){
		$scope.store.thumbnails.splice(idxVal, 1);
	}

	$scope.Submit = function(){
		$http.post('/save-store', $scope.store).success(function(response) {
	      if(response.status===200){
	      	alert(response.messages, $location.path("/"));
	      } 
	      else{
	      	alert(response.messages);	
	      }
	    });
	}

	$scope.Cancel = function(){
		$location.path("/");
	}
}

