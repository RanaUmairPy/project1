from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    s_class = models.CharField(max_length=50,null=True, blank=True)




class CustomUser(AbstractUser):
    pass

