from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

class forYou(models.Model):
    #field that accepts url type in database
    link = models.URLField(max_length=200)
    description = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)#auto_now_add automatically populates the field with time that the node is created
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fory")
    #user means we would want to fill the column user by loggedin user from other table using foreign key
    #on delete cascade means if a user is deleted all the data linked to that user also gets deleted
    #related name is for identification of relationship between two tables

