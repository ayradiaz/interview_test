(function(){
    'use strict';

    var app = angular.module('ocom.exam', ['ngRoute']);
    app.config(function($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl : "/static/js/project-list.html"
            })
            .when("/add", {
                templateUrl : "/static/js/add-project.html"
            })
            .when("/update", {
                templateUrl : "/static/js/update-project.html"
            });
    });

}());