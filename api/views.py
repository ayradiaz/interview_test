import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from .models import Library, LibraryEntries, Project

@csrf_exempt
@api_view(('POST',))
def new_project(request):
    """
    method for non api requests for adding new project

    """

    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)


    libraries = data.get('libraries')

    #p = Project(**data)
    name = data.get('name')
    active_start_date = data.get('active_start_date')
    active_end_date = data.get('active_end_date')
    client_name = data.get('client_name')
    description = data.get('description')
    git_url = data.get('git_url')
    testing_url = data.get('testing_url')
    production_url = data.get('production_url')

    p = Project.objects.create(name=name,active_start_date=active_start_date,
                               active_end_date=active_end_date,client_name=client_name,
                               description=description,git_url=git_url,testing_url=testing_url,
                               production_url=production_url)
    for key in libraries:
        lib_id = key["id"]
        lib = LibraryEntries.objects.get(id=lib_id)
        p.libraries.add(lib)
    return Response(status=HTTP_200_OK)


@csrf_exempt
@api_view(('POST',))
def edit_project(request):
    """
    method for non api requests edit

    """

    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)


    libraries = data.get('libraries')


    project_id = data.get('id')

    p = Project.objects.get(id=project_id)

    p.name = data.get('name')
    p.active_start_date = data.get('active_start_date')
    p.active_end_date = data.get('active_end_date')
    p.client_name = data.get('client_name')
    p.description = data.get('description')
    p.git_url = data.get('git_url')
    p.testing_url = data.get('testing_url')
    p.production_url = data.get('production_url')

    p.save()

    p.libraries.clear()
    for key in libraries:
        lib_id = key["id"]
        lib = LibraryEntries.objects.get(id=lib_id)
        p.libraries.add(lib)

    return Response(status=HTTP_200_OK)


@csrf_exempt
@api_view(('POST',))
def delete_project(request):
    """
    method for non api requests edit

    """
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    project_id = data

    p = Project.objects.get(id=project_id)
    p.delete()

    return Response(status=HTTP_200_OK)