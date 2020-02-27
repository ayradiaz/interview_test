
(function(){
    'use strict';

    var app = angular.module('ocom.exam',[]);

    var ProjectController = function($scope, $http) {
        $scope.projects = [];
        $scope.new_project = {};


        var onGetProject = function(response){
            $scope.projects = response.data
        };

        var onError = function(reason){
            $scope.error = "Could not fetch data"
        }

        var addProject = function (){
            console.log('add project called');
            var new_project = $scope.new_project;
            new_project.libraries = [];

            for (var i = 0; i < $scope.libraries.length; i++) {
                if ($scope.libraries[i].checked) {
                    new_project.libraries.push({
                        id: $scope.libraries[i].id,
                    });
                }
            }
            console.log(new_project);
            $http.post('create/projects/', new_project).then(function(response){
                console.log('post here', response);
                $scope.projects.push(response.data);
            }, function() {
                console.log('error creating new project');
            });


        }

        console.log('hello');
        $scope.libraryEntries = [];
        $scope.addProject = addProject;



        $http.get('/projects/').then(onGetProject, onError);

        $http.get('/libraryentries/').then(function (response) {
            $scope.libraries = response.data;});
    };

     app.controller("ProjectController", ["$scope", "$http", ProjectController]);
}());
