from django.db import models
from django.contrib.auth.models import *



class Tags(models.Model):
    topic = models.CharField(max_length=50)
    
    def __str__(self):
        return self.topic

class Asset(models.Model):
    image = models.ImageField(upload_to='media', blank=True)

class Content(models.Model):
    text = models.CharField(max_length=10000)

    def __str__(self):
        return self.text

class Author(models.Model):
    name = models.CharField(max_length =50)
    avatar = models.ForeignKey(Asset)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    content = models.ForeignKey(Content)
    asset = models.ForeignKey(Asset)
    title = models.CharField(max_length=255)
    post_like = models.IntegerField()
    date = models.DateField()
    tags = models.ManyToManyField(Tags)
    post_author = models.ForeignKey(Author)

    def __str__(self):
        return self.title







        



