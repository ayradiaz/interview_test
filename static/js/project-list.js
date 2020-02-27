(function(){
    'use strict';

    var ProjectListController = function($scope, $http, $routeParams, $location) {
        $scope.projects = [];
        $scope.deleteProject = deleteProject;
        
        loadProjects();

        function loadProjects() {
            $http.get('/projects/').then(function(response){
                $scope.projects = response.data
            }, function(reason){
                $scope.error = 'Could not fetch data'
            });
        }

        function deleteProject(projectID) {
            var project = projectID;

            $http.post('/delete/projects/', project).then(function(response){
                console.log('post here', response);
                loadProjects();
            }, function() {
                console.log('error deleting  project');
            });

        }
    };

     angular.module('ocom.exam').controller('ProjectListController', ['$scope', '$http', '$routeParams','$location', ProjectListController]);
}());

