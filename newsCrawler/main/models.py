from django.db import models
from scrapy_djangoitem import DjangoItem

class article(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class unclassiedArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class defenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class nonDefenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class AIdefenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class AInonDefenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    date =models.TextField()
    url=models.URLField(max_length=255)
    description=models.TextField()

class articleItem(DjangoItem):
    django_model = article