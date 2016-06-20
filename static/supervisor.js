var GLOBAL_URL_NEWEQUIP 	= "/equipment/create";
var GLOBAL_URL_DELEQUIP		= "/equipment/delete";
var GLOBAL_URL_GETEQUIPS	= "/equipment/get";

var GLOBAL_URL_NEWDELEG 	= "/delegation/create";
var GLOBAL_URL_DELDELEG 	= "/delegation/delete";
var GLOBAL_URL_GETDELEGS	= "/delegation/get";

var GLOBAL_URL_NEWEMP		= "/employee/create"
var GLOBAL_URL_GETEMP		= "/employee/get"
var GLOBAL_URL_DELEMP 		="/employee/delete"

var GLOBAL_URL_NEWFACILITY 	= "/facility/create";
var GLOBAL_URL_NEWLANGUAGE	="/language/create";

///////////
//MDL JS //
///////////

function showSnackbar(msg){ 
	var notification = document.querySelector('#snackbar-show'); 
	var data = { 
		message: msg, 
		timeout: 2000
	}; 
	notification.MaterialSnackbar.showSnackbar(data); 
} 


////////////
//ANGULAR //
////////////

var angApp = angular.module("flask-paratrack", []);

angApp.factory('BackendService', function($http) {
	return {
		'newEquip': function(data) {
			return $http.post(GLOBAL_URL_NEWEQUIP, data);
		},

		'delEquip': function(data) {
			return $http.post(GLOBAL_URL_DELEQUIP, data);
		},

		'newDeleg': function(data) {
			return $http.post(GLOBAL_URL_NEWDELEG, data);
		},

		'newLanguage': function(data) {
			return $http.post(GLOBAL_URL_NEWLANGUAGE, data);
		},
		
		'delDeleg': function(data) {
			return $http.post(GLOBAL_URL_DELDELEG, data);
		},

		'newFacility': function(data) {
			return $http.post(GLOBAL_URL_NEWFACILITY, data);
		},

		'getAllEquips': function(data) {
			return $http.post(GLOBAL_URL_GETEQUIPS, data);
		},

		'getAllDelegations': function(data) {
			return $http.post(GLOBAL_URL_GETDELEGS, data);
		},

		'getAllEmployees': function(data) {
			return $http.post(GLOBAL_URL_GETEMP, data);
		},

		'newEmployee': function(data) {
			return $http.post(GLOBAL_URL_NEWEMP, data);
		},

		'delEmployee': function(data) {
			return $http.post(GLOBAL_URL_DELEMP, data);
		}
	}
});

angApp.controller('MainController', ['$scope', 'BackendService', 
	function($scope, BackendService) { 


	angular.isUndefinedOrNull = function(val) {
		return angular.isUndefined(val) || val === null 
	}

	$scope.getAllEquips = function(){

		BackendService.getAllEquips(null).then(
		function(response) {
			console.info(response);
			if(response.data.success){
				console.info("[getAllEquips] Success!");
				console.info(response.data);
				$scope.allPackages = response.data.list
			} else {
				console.info("[getAllEquips] Failed!");
			}
		},
		function(response) {
			showSnackbar("Server error. Contact the devs.");
			console.info("[getAllEquips] Error received!");
		}
		);
	}
	
	$scope.delEquip = function(idx){
		pkg = $scope.allPackages[idx];

		if(pkg && pkg.id){
			data = {id: pkg.id};

			BackendService.delEquip(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[Delequip] Success!");
						console.info(response.data);
						$scope.allPackages.splice(idx, 1)
						showSnackbar("Equipment deleted!");
					} else {
						console.info("[Delequip] Failed!");
						showSnackbar(response.data.msg)
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[Newequip] Error received!");
				}
			);
		} else {
			showSnackbar("Please refresh the section before doing that.");
		}
	}

	$scope.delDeleg = function(idx){
		deleg = $scope.allDelegations[idx];

		if(deleg){
			data = {d_name: deleg.name};

			BackendService.delDeleg(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[DelDeleg] Success!");
						console.info(response.data);
						$scope.allDelegations.splice(idx, 1)
						showSnackbar("Delegation deleted!");
					} else {
						console.info("[DelDeleg] Failed!");
						showSnackbar(response.data.msg)
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[DelDeleg] Error received!");
				}
			);
		}
	}

	$scope.getAllDelegations = function(){

		BackendService.getAllDelegations(null).then(
		function(response) {
			console.info(response);
			if(response.data.success){
				console.info("[getAllDelegations] Success!");
				console.info(response.data);
				$scope.allDelegations = response.data.list
			} else {
				console.info("[getAllDelegations] Failed!");
			}
		},
		function(response) {
			showSnackbar("Server error. Contact the devs.");
			console.info("[getAllDelegations] Error received!");
		}
		);
	}

	$scope.getAllEmployees = function(){

		BackendService.getAllEmployees(null).then(
		function(response) {
			console.info(response);
			if(response.data.success){
				console.info("[getAllEmployees] Success!");
				console.info(response.data);
				$scope.allEmployees = response.data.list
			} else {
				console.info("[getAllEmployees] Failed!");
			}
		},
		function(response) {
			showSnackbar("Server error. Contact the devs.");
			console.info("[getAllEmployees] Error received!");
		}
		);
	}

	$scope.delEmployee = function(idx){
		emp = $scope.allEmployees[idx];

		if(emp){
			data = {CPF: emp.CPF};

			BackendService.delEmployee(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[Delequip] Success!");
						console.info(response.data);
						
						$scope.allEmployees.splice(idx, 1)
						
						showSnackbar("Employee fired!");
					} else {
						console.info("[Delequip] Failed!");
						showSnackbar(response.data.msg)
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[Delequip] Error received!");
				}
			);
		}
	}

	$scope.editableEquip = function(idx){
		pack = $scope.allPackages[idx];

		if(!angular.isUndefinedOrNull(pack.editable))
			if (pack.editable == false)
				pack.editable = true;
			else pack.editable = false;
		else pack.editable = true;
	}

	$scope.submitPkg = function (){

		if (
			angular.isUndefinedOrNull($scope.pkg_name)			|| 
			angular.isUndefinedOrNull($scope.pkg_owner)			|| 
			angular.isUndefinedOrNull($scope.pkg_desc)
			){
			showSnackbar("Missing field...");

		} else {
			var data = {
				e_name: 		$scope.pkg_name,
				owner: 			$scope.pkg_owner,
				description: 	$scope.pkg_desc,
				name: 			$scope.pkg_name
			}

			BackendService.newEquip(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[Newequip] Success!");
						console.info(response.data);
						showSnackbar("Equipment registered!");

						$scope.allPackages.unshift(data);

					} else {
						console.info("[Newequip] Failed!");
						showSnackbar(response.data.msg)
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[Newequip] Error received!");
				}
			);
		}
	}

	$scope.submitDeleg = function (){

		if (
			angular.isUndefinedOrNull($scope.deleg_name)			|| 
			angular.isUndefinedOrNull($scope.deleg_country)
			){
			showSnackbar("Missing field...");

		} else {
			var data = {
				d_name: 	$scope.deleg_name,
				country: 	$scope.deleg_country,
				email: 		$scope.deleg_email ? $scope.email : "",
				tel: 		$scope.deleg_tel ? $scope.deleg_tel : "",
				name: 		$scope.deleg_name
			}

			BackendService.newDeleg(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[Newdeleg] Success!");
						console.info(response.data);
						showSnackbar("Delegation created!");

						$scope.allDelegations.unshift(data);

					} else {
						showSnackbar(response.data.msg)
						console.info("[Newdeleg] Failed!");
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[Newdeleg] Error received!");
				}
			);
		}
	}

	$scope.submitEmployee = function (){

		if (
			angular.isUndefinedOrNull($scope.emp_CPF)	||
			angular.isUndefinedOrNull($scope.emp_RG)	||
			angular.isUndefinedOrNull($scope.emp_name)	||
			angular.isUndefinedOrNull($scope.emp_work)	||
			angular.isUndefinedOrNull($scope.emp_password)
			){
			showSnackbar("Missing field...");

		} else {
			var data = {
				CPF: 	$scope.emp_CPF,
				RG: 	$scope.emp_RG,
				name:	$scope.emp_name,
				work_on:$scope.emp_work,
				password:$scope.emp_password
			}

			BackendService.newEmployee(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[NewEmployee] Success!");
						console.info(response.data);
						showSnackbar("Employee created!");

						$scope.allEmployees.unshift(data);

					} else {
						showSnackbar(response.data.msg)
						console.info("[NewEmployee] Failed!");
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[NewEmployee] Error received!");
				}
			);
		}
	}

	$scope.submitFacility = function (){

		if (
			angular.isUndefinedOrNull($scope.facility_name)
			){
			showSnackbar("Missing field...");

		} else {
			var data = {
				f_name: 	$scope.facility_name,
				address: 	$scope.facility_address ? $scope.facility_address : "",
				capacity:	$scope.facility_capacity ? $scope.facility_capacity : ""
			}

			BackendService.newFacility(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[NewFacility] Success!");
						console.info(response.data);
						showSnackbar("Facility created!");
					} else {
						showSnackbar(response.data.msg)
						console.info("[NewFacility] Failed!");
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[Newdeleg] Error received!");
				}
			);
		}
	}

	$scope.submitLanguage = function (){
		console.info($scope.emp_lang_CPF)
		console.info($scope.emp_lang)
		if (
			angular.isUndefinedOrNull($scope.emp_lang_CPF) ||
			angular.isUndefinedOrNull($scope.emp_lang)
			){
			showSnackbar("Missing field...");

		} else {

			var data = {
				CPF: 		$scope.emp_lang_CPF,
				language: 	$scope.emp_lang
			}

			BackendService.newLanguage(data).then(
				function(response) {
					console.info(response);
					if(response.data.success){
						console.info("[NewLanguage] Success!");
						console.info(response.data);
						showSnackbar("Employee language created!");
					} else {
						showSnackbar(response.data.msg)
						console.info("[NewLanguage] Failed!");
					}
				},
				function(response) {
					showSnackbar("Server error. Contact the devs.");
					console.info("[NewLanguage] Error received!");
				}
			);
		}
	}

	// STARTUP FUNCTIONS
	
	$scope.refresh = function() {
		$scope.getAllEquips();
		$scope.getAllDelegations();
		$scope.getAllEmployees();
	}

	$scope.refresh();

}]);

