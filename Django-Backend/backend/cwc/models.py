from django.db import models
import uuid
from django.utils import timezone
class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)
    
    # def login
# Create your models here.
class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    owner = models.CharField(max_length=20)
    club = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField(default = "", max_length=500)
    # created_at = models.DateTimeField(editable=False, null=True, blank=True)
    # updated_at = models.DateTimeField()
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         print(222)
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #     return super(Post, self).save(*args, **kwargs)
