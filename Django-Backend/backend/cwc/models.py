from django.db import models

class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    
    # def login
# Create your models here.
