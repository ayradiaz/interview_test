(function(){
    'use strict';

    var UpdateProjectController = function($scope, $http, $routeParams, $location) {
        $scope.project = {};
        $scope.libraries = [];
        $scope.save = save;

        loadLibraryEntries(loadProject);

        function save() {
            var project = $scope.project;
            project.libraries = [];

            for (var i = 0; i < $scope.libraries.length; i++) {
                if ($scope.libraries[i].checked) {
                    project.libraries.push({
                        id: $scope.libraries[i].id,
                        version: $scope.libraries[i].version_number
                    });
                }
            }

            console.log(project);

            var timezoneOffset = (new Date()).getTimezoneOffset();
            if ($scope.project.active_start_date) {
                var activeStartDateLocal = moment($scope.project.active_start_date).add(-timezoneOffset, 'm').format('YYYY-MM-DD');
                project.active_start_date = activeStartDateLocal;
            }
            if ($scope.project.active_end_date) {
                var activeEndDateLocal = moment($scope.project.active_end_date).add(-timezoneOffset, 'm').format('YYYY-MM-DD');
                project.active_end_date = activeEndDateLocal;
            }

            $http.post('/edit/projects/', project).then(function(response){
                console.log('post here', response);
                $location.path('/');
            }, function() {
                console.log('error updating new project');
            });
        }

        function loadLibraryEntries(additionalSuccessCallback) {
            $http.get('/libraryentries/').then(function (response) {
                $scope.libraries = response.data;

                if (additionalSuccessCallback) {
                    additionalSuccessCallback();
                }
            });
        }

        function loadProject() {
            console.log($routeParams);
            $http.get('/projects/' + $routeParams.projectId).then(function (response) {
                console.log(response);
                $scope.project = response.data;
                console.log($scope.libraries);
                console.log($scope.project.libraries);
                for (var i = 0; i < $scope.project.libraries.length; i++) {
                    for (var j = 0; j < $scope.libraries.length; j++) {
                        if ($scope.project.libraries[i].id === $scope.libraries[j].id) {

                            $scope.libraries[j].checked = true;
                            break;
                        }
                    }
                }
            });
        }
    };

     angular.module('ocom.exam').controller('UpdateProjectController', ['$scope', '$http', '$routeParams', '$location', UpdateProjectController]);
}());