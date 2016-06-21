var GLOBAL_URL_NEWEQUIP 	= "/equipment/create";
var GLOBAL_URL_DELEQUIP		= "/equipment/delete";
var GLOBAL_URL_GETEQUIPS	= "/equipment/get";

var GLOBAL_URL_NEWDELEG 	= "/delegation/create";
var GLOBAL_URL_DELDELEG 	= "/delegation/delete";
var GLOBAL_URL_GETDELEGS	= "/delegation/get";

var GLOBAL_URL_TRANSLATOR	="/translator/get";

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
		
		'delDeleg': function(data) {
			return $http.post(GLOBAL_URL_DELDELEG, data);
		},

		'getAllEquips': function(data) {
			return $http.post(GLOBAL_URL_GETEQUIPS, data);
		},

		'getAllDelegations': function(data) {
			return $http.post(GLOBAL_URL_GETDELEGS, data);
		},

		'getTranslator': function(data) {
			return $http.post(GLOBAL_URL_TRANSLATOR, data);
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

	$scope.editableEquip = function(idx){
		pack = $scope.allPackages[idx];

		if(!angular.isUndefinedOrNull(pack.editable))
			if (pack.editable == false)
				pack.editable = true;
			else pack.editable = false;
		else pack.editable = true;
	}

	$scope.closeTranslators = function(){
		$scope.translators_flag = false;
		$scope.allTranslators = {}
	}

	$scope.getTranslator = function(){

		var data = {
			language: $scope.translator_lang ? $scope.translator_lang : ""
		}

		BackendService.getTranslator(data).then(
			function(response) {
				console.info(response);
				if(response.data.success){
					console.info("[Translator] Success!");
					console.info(response.data);
					$scope.translators_flag = true;

					var array = [];
					var flag = false;

					for (var i = 0; i < response.data.list.length; i++) {
						flag = false;
						for (var j = 0; j < array.length; j++) {
							if(array[j].name == response.data.list[i].name){
								array[j].language += response.data.list[i].language
								flag = true;
								break;
							}
						}
						if(!flag){
							var new_emp = response.data.list[i];
							var lang = new_emp.language;
							new_emp.language = [lang];
							array.push(new_emp);1
						}
					}

					$scope.allTranslators = array;

				} else {
					showSnackbar(response.data.msg)
					console.info("[Translator] Failed!");
				}
			},
			function(response) {
				showSnackbar("Server error. Contact the devs.");
				console.info("[Translator] Error received!");
			}
		);
	}



	// STARTUP FUNCTIONS
	
	$scope.refresh = function() {
		$scope.getAllEquips();
		$scope.getAllDelegations();
	}

	$scope.refresh();

}]);

