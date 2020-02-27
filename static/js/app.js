(function(){
    'use strict';

    var app = angular.module('ocom.exam', ['ngRoute', 'ngMaterial', 'ngMessages',]);
    app.config(function($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl : "/static/html/project-list.html"
            })
            .when("/add", {
                templateUrl : "/static/html/add-project.html"
            })
            .when("/update", {
                templateUrl : "/static/html/update-project.html"
            });
    });

}());