from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Cake(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    email=models.EmailField(max_length=200)
    mobilenumber=models.CharField(max_length=10,null=False,blank=False)
    address=models.CharField(max_length=200,null=False,blank=False)
    quantity=models.CharField(max_length=10,null=True,blank=False)
    description=models.TextField()





