from django.db import models

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['username', 'email', 'password']

    def __str__(self):
        # username and is_staff are attributes of the User class
       return self.username + " " + str(self.is_staff)
# Compare this snippet from crud_api_project\user\apps.py:
# from django.apps import AppConfig
#

# class UserConfig(AppConfig):

