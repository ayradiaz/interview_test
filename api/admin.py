from django.contrib import admin

from .models import Library, LibraryEntries, Project

admin.site.register(Library)
admin.site.register(LibraryEntries)
admin.site.register(Project)
