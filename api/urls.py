from django.urls import path
from .api import ProjectViewSet, LibraryEntriesViewSet, LibraryViewSet
from rest_framework.routers import DefaultRouter
from .views import new_project, edit_project, delete_project

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('libraryentries',LibraryEntriesViewSet)
router.register('library', LibraryViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('create/projects/', new_project, name='new_project'),
    path('edit/projects/', edit_project, name='edit_project'),
    path('delete/projects/', delete_project, name='delete_project'),
]