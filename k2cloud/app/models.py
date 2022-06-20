from importlib.metadata import requires
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField( null = False, max_length=100)
    Contact = models.CharField(null = False, max_length=20)
    Email = models.EmailField(null = False)
    Message = models.CharField(null = False, max_length=1000)