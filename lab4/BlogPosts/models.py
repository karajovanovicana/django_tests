from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/")
    interests = models.TextField(max_length=500)
    skills = models.TextField(max_length=500)
    profession = models.CharField(max_length=200)
    blocked_user = models.ManyToManyField(User, related_name='blocked_user', blank=True)

    def __str__(self):
        return self.name + " " + self.surname


class Post(models.Model):
    title = models.CharField(max_length=70)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    file = models.FileField(upload_to="files/")
    date_created = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
