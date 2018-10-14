from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.dispatch import receiver

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
    def search_detail(cls,search_term):
        detail = cls.objects.filter(user__username___icontains=search_term)
        return detail

    @classmethod
    def get_by_id(cls, id):
        detail = Detail.objects.get(id=id)
        return detail


class Image(models.Model):
    post = models.ImageField(upload_to = 'users/', blank=True)
    caption = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pub_date']

    def save_image(self):
        self.save()

    def delete_image():
        self.delete()

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    @property
    def count_likes(self):
        likes = self.likes.count()
        return likes
    
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.filter(user_id=id).all()
        return image

    def __str__(self):
        return self.caption

class Comment(models.Model):
    comment = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")
    class Meta:
        ordering = ['pub_date']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment_by_image_id(cls,image):
        comments = Comments.objects.get(image_id=image)
        return comments

    def __str__(self):
        return self.comment 

class Likes(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    liked_post =models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes')

    def save_like(self):
        self.save()

    def __str__(self):
        return self.user_like


