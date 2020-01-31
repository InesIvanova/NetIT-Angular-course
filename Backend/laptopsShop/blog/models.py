from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    author = models.CharField(max_length=255, default="Unknown")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
