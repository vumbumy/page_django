from django.db import models


# Create your models here.
class Job(models.Model):
    started = models.DateField()
    ended = models.DateField(null=True, blank=True)

    company = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.company

    class Meta:
        ordering = ['-started']


class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Job', on_delete=models.PROTECT, null=True)

    started = models.DateField()
    ended = models.DateField(null=True, blank=True)

    env = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-started']


class History(models.Model):
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)

    category = models.SlugField(max_length=10, default="")
    description = models.TextField()

    def __str__(self):
        return self.project.name
