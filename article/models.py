from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comment', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.text


class BlockList(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
