from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,default="Empty")
    avatar = models.ImageField(upload_to='Avatar/', default='default.jpg')

    def __str__(self):
        str = self.user.username    
        return str
