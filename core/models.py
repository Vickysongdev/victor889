from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)
    profiling = models.ImageField(upload_to='profiling_images', default='avater.png.jpg',)
    location = models.CharField(max_length=100, blank=True,)




def __str__(self):
    return self.user.username

