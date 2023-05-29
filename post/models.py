from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Post(models.Model):
    images = models.ManyToManyField('Image')
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    created_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status = models.BooleanField()



# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username