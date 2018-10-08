from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    title = models.CharField(max_length = 60)
    Name = models.TextField()
    profile_image = models.ImageField(upload_to = 'users')
