(function(){
    'use strict';

    var AddProjectController = function($scope, $http, $location) {
        $scope.new_project = {};
        $scope.libraries = [];
        $scope.addProject = addProject;
        $scope.message = "";

        loadLibraryEntries();

        function addProject() {
            var new_project = $scope.new_project;
            new_project.libraries = [];

            for (var i = 0; i < $scope.libraries.length; i++) {
                if ($scope.libraries[i].checked) {
                    new_project.libraries.push({
                        id: $scope.libraries[i].id,
                        version: $scope.libraries[i].version_number
                    });
                }
            }

            console.log(new_project);

            $http.post('create/projects/', new_project).then(function(response){
                $scope.message = "New Project Added";
                $location.path('/');
            }, function() {
                console.log('error creating new project');
            });
        }

        function loadLibraryEntries() {
            $http.get('/libraryentries/').then(function (response) {
                $scope.libraries = response.data;
            });
        }
    };

     angular.module('ocom.exam').controller('AddProjectController', ['$scope', '$http', '$location', AddProjectController]);
}());