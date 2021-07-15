from django.db import models
from scrapy_djangoitem import DjangoItem

class article(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    url=models.URLField(max_length=255)
    description=models.TextField()

class defenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    url=models.URLField(max_length=255)
    description=models.TextField()

class nonDefenceArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    url=models.URLField(max_length=255)
    description=models.TextField()

class mlArticle(models.Model):
    heading = models.CharField(max_length=255, unique = True)
    url=models.URLField(max_length=255)
    description=models.TextField()

class articleItem(DjangoItem):
    django_model = article