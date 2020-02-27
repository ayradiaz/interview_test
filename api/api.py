from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectSerializer, LibraryListSerializer, LibrarySerializer
from .models import Project, LibraryEntries, Library


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LibraryEntriesViewSet(ModelViewSet):
    queryset = LibraryEntries.objects.all()
    serializer_class = LibraryListSerializer


class LibraryViewSet(ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer