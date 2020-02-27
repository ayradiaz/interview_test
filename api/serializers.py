from rest_framework import serializers

from .models import Project, LibraryEntries, Library


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = '__all__'


class LibraryListSerializer(serializers.ModelSerializer):
    library = serializers.CharField(source='library.description')

    class Meta:
        model = LibraryEntries
        fields = ['id','library','version_number']


class ProjectSerializer(serializers.ModelSerializer):
    libraries = LibraryListSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id","name","active_start_date","active_end_date","description",
                  "client_name","git_url","testing_url",
                  "production_url","libraries"]