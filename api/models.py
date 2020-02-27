import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


class Library(models.Model):
    description = models.CharField(max_length=250, blank=False)
    active_start_date = models.DateField(default=datetime.date.today)
    active_end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = _("Library")

    def __str__(self):
        return self.description


class LibraryEntries(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=10, blank=False)

    class Meta:
        verbose_name_plural = _("Library Entries")

    def __str__(self):
        library = self.library.description
        return '%s %s' % (self.library, self.version_number)



class Project(models.Model):
    name = models.CharField(max_length=30, blank=False)
    active_start_date = models.DateField(default=datetime.date.today)
    active_end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    client_name = models.CharField(max_length=100, blank=False)
    git_url = models.CharField(max_length=250, blank=False)
    testing_url = models.CharField(max_length=250, blank=True)
    production_url = models.CharField(max_length=250, blank=True, null=True)
    libraries = models.ManyToManyField(LibraryEntries, blank=True)

    def __str__(self):
        return self.name
