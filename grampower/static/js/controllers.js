'use strict';

/* Controllers */

function IndexController($scope, $http, $rootScope,localResource, $location, $window) {
    $scope.storeList = [];
    $scope.currentFetch = []; 
    $scope.scrollPos = 0;
    $scope.scrollHeight = 0;
    $scope.pageNo = 0;
    $scope.loadData = function(){
        $scope.currentFetch = [];
        $http.get('/stores-all?page='+$scope.pageNo).success(function(response) {
            $scope.currentFetch = response.data;
            Array.prototype.push.apply($scope.storeList, $scope.currentFetch);
        });
    };
    $scope.loadData();
    
    $window.onscroll = function(){
        $scope.scrollPos = document.body.scrollTop || document.documentElement.scrollTop || 0;
        $scope.scrollHeight = document.body.scrollHeight;
        $scope.scrollPos += window.innerHeight + 10; 
        if($scope.scrollPos>=$scope.scrollHeight){  
            if($scope.currentFetch.length>=10){
                $scope.pageNo+=1;
                $scope.loadData();
            }
        }
        $scope.$apply(); 
    };
    
    $scope.dayList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    $scope.ShowTime = function(inVal){
        var myDate = new Date();
        for(var i=0; i<inVal.length; i++){
            if($scope.dayList[myDate.getDay()] === inVal[i].name){
                if(inVal[i].status === true){
                    return 'Opens at '+ inVal[i].open;
                }else{
                    return 'Closed on ' + $scope.dayList[myDate.getDay()];
                }
            }
        }
    }
    
 	$scope.Category = function(store){
        $scope.categoryJoin = '';
    	$scope.categoryJoin = localResource.joinList(store.pro_categories);
        return $scope.categoryJoin;
 	}
    
    $scope.JoinAddress = function(street_address, city, postal_code){
        $scope.fullAddress = '';
        $scope.fullAddress =  street_address + ', ' + city + ' - ' + postal_code; 
        return $scope.fullAddress;
    }
    
  	$scope.StoreClicked = function(idxVal,index){
        $location.path('/store/').search({id: idxVal});        
        $rootScope.address = $scope.storeList[index].street_address+','+$scope.storeList[index].city+'-'+$scope.storeList[index].postal_code;
  	};
}



function StoreController($scope, $rootScope, localResource, $http, $location, NgMap) {
	var queryString = $location.search();
	$http.get('/get-store?id='+queryString.id).success(function(response) {
    	$scope.store = response.data;
		$scope.address = $scope.store.street_address+','+$scope.store.city+'-'+$scope.store.postal_code;
    	$scope.categories = [];
    	$scope.categories = localResource.joinList($scope.store.pro_categories);
   	});	

  	var modal = document.getElementById('myModal');   
	var modalImg = document.getElementById("img01");

	$scope.OpenModal = function(src){
		var oldSrc = src;
		var str = oldSrc.replace(/thumbnail/g,"img");
		$scope.src = str;
	    modal.style.display = "block";
	    modalImg.src = str;
	};

	$scope.CloseModal = function(){
		modal.style.display = "none";
	};	
}


function RegisterController($scope, $location, $http) {
    $scope.onlyNumbers = /^\d+$/;
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
            status: false,
            open: '',
            close: '',
        },{
            name: 'Tuesday',
            status: false,
            open: '',
            close: '',
        },{
            name: 'Wednesday',
            status: false,
            open: '',
            close: '',
        },{
            name: 'Thursday',
            status: false,
            open: '',
            close: '',
        },{
            name: 'Friday',
            status: false,
            open: '',
            close: '',
        },{
            name: 'Saturday',
            status: false,
            open: '',
            close: '',
        },{
            name: 'Sunday',
            status: false,
            open: '',
            close: '',
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
            status: false,
        },],
        latitude: '',
        longitude: '', 
    };

    $scope.workingHoursArray = ['01','02','03','04','05','06','07','08','09','10','11'];
    $scope.workingMinsArray = [];
    for(var i=0;i<60;i++){
        if(i<10){
            $scope.workingMinsArray.push('0'+i);
        }else{
            $scope.workingMinsArray.push(i.toString());
        }       
    };
     $scope.workingMiddayArray = ['AM','PM'];

    $scope.workingHours={
        'Monday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Tuesday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Wednesday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Thursday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Friday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Saturday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        },
        'Sunday':{
            startDate:{
                hours: '09',
                mins:'00',
                midday: 'AM'
            },
            endDate:{
                hours: '05',
                mins:'00',
                midday: 'PM'
            }
        }
    }
 

    $scope.addToThumbnail = function(){
        $scope.store.thumbnails.push($scope.currentImage);
        $scope.currentImage = '';
    };

    $scope.removeThumbnail = function(idxVal){
        $scope.store.thumbnails.splice(idxVal, 1);
    }

    $scope.Submit = function(){
        if($scope.store.name.trim() === '' || $scope.store.licence_no.trim() === '' || $scope.store.street_address.trim() === '' || $scope.store.postal_code.trim() === '' || $scope.store.city.trim() === '' || $scope.store.contact_number.trim() === '' || $scope.store.cover_image.trim() === '' || $scope.store.description.trim() === ''){
            $scope.missingMandatoryFields = true;
            return;
        }
        var dateCheck = false;
        for (var j=0;j<$scope.store.working_days.length;j++){
            if($scope.store.working_days[j].status === true){
                dateCheck = true;
                var currentItemData = $scope.store.working_days[j];
                $scope.store.working_days[j].open = $scope.workingHours[currentItemData.name].startDate.hours+":"+$scope.workingHours[currentItemData.name].startDate.mins+" "+$scope.workingHours[currentItemData.name].startDate.midday;
                $scope.store.working_days[j].close = $scope.workingHours[currentItemData.name].endDate.hours+":"+$scope.workingHours[currentItemData.name].endDate.mins+" "+$scope.workingHours[currentItemData.name].endDate.midday;
            }
        }
        if(dateCheck === false){
            $scope.missingMandatoryFields = true;
            return;
        }
        var categoryCheck = false;
        for(var i = 0; i<$scope.store.pro_categories.length; i++){
            if($scope.store.pro_categories[i].status === true){
                categoryCheck = true;
            }
        }
        if(categoryCheck === false){
            $scope.missingMandatoryFields = true;
            return;
        }
         $http.post('/save-store', $scope.store).success(function(response) {
          if(response.status===200){
             alert("Store inserted Successfully", $location.path("/"));
          } 
          else{
            alert(response.messages);   
          }
        });
    }

    $scope.Cancel = function(){
        $location.path("/");
    }
    
    $scope.myImage='';
    $scope.myCroppedImage='';
    $scope.displayCroppedImg = false;

    var handleFileSelect=function(evt) {
      $scope.displayCroppedImg = false;
      $scope.cropDone = false;
      var file=evt.currentTarget.files[0];
      var reader = new FileReader();
      reader.onload = function (evt) {

        $scope.$apply(function($scope){
          $scope.myImage=evt.target.result;
        });
       };
      reader.readAsDataURL(file);
    };

    angular.element(document.querySelector('#fileInput')).on('change',handleFileSelect);
}


