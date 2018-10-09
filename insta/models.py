from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.dispatch import receiver



class Profile(models.Model):
    title = models.CharField(max_length = 60)
    caption = models.TextField()
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to = 'users/')


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

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Detail(models.Model):
    bio = HTMLField()
    user_image = models.ImageField(upload_to ='users/')
    user = models.OneToOneField(User, on_delete=models.CASCADE,null="True")

    @receiver(post_save, sender=User)
    def create_user_detail(sender,instance,created, **kwrgs):
        if created:
            Detail.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_detail(sender, instance, **kwargs):
        instance.detail.save()

    post_save.connect(save_user_detail,sender=User)

    def save_detail(self):
        self.save()

    @classmethod
    def search_detail(cls,name):
        detail = cls.objects.filter(user__username___icontains=name)
        return detail

    @classmethod
    def get_by_id(cls, id):
        detail = Detail.objects.get(id=id)
        return detail


