from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ArticleTypes(models.Model):
    name=models.CharField(max_length=100)
    fields = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

class Articles(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    about = models.TextField(max_length=1500)
    fields = models.JSONField(default='', blank=True)

    def __str__(self):
        return self.name