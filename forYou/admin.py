from django.contrib import admin

# '.' represents from this folder
# we are importing our custom model of newly created app
from . import models 

#we specify the class here so as to display our model changes in the admin interface
# Register your models here.
class forYouAdmin(admin.ModelAdmin): #this class should inherit from admin model admin
    list_display=('description','link') #this tuple is used to tell django admin how to display the details in the table
    

#we will have to register the custom model and the class to admin model so as to display it in admin interface
admin.site.register(models.forYou, forYouAdmin) #two arguments one is custom model and custom models class