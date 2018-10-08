from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Profile(models.Model):
    title = models.CharField(max_length = 60)
    Name = models.TextField()
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to = 'users/')

    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post

    @classmethod
    def todays_post(cls):
        post = cls.objects.filter(title__icontains=search_term)
        return post

    @classmethod
    def all_post():
        post = cls.object.all()
        return post

    def __str__(self):
        return self.title