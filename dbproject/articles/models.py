from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fields(models.Model):
    born = models.CharField(max_length=100)
    died = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    knownFor = models.CharField(max_length=100)
    notableWork = models.TextField(max_length=1000)

    class Meta:
        abstract = True

class Articles(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    fields = models.JSONField(default=dict)

    def __str__(self):
        return self.name