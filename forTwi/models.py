from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class forTwi(models.Model):
    #field that accepts url type in database
    link = models.URLField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)#auto_now_add automatically populates the field with time that the node is created
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fort")
    