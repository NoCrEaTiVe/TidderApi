from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    user = models.OneToOneField(User,on_delete=models.CASCADE,parent_link=True)
    rating = models.IntegerField(default=0)
    communities = models.ManyToManyField('Community')
    followers = models.ManyToManyField('self', related_name='follower',blank=True)
    following = models.ManyToManyField('self', related_name='following',blank=True)



class Post(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    community = models.ForeignKey('Community',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True,null=True)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='posts',default='static/')


class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
