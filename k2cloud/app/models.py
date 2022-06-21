from importlib.metadata import requires
from django.db import models
import datetime
# Create your models here.
class Contact(models.Model):
    Name = models.CharField( null = False, max_length=100)
    Contact = models.CharField(null = False, max_length=20)
    Email = models.EmailField(null = False)
    Message = models.CharField(null = False, max_length=1000)
    postedOn =models.DateTimeField(default=datetime.datetime.now(), null = False )

    def __str__(self):
        return self.Name + " - " + str(self.postedOn.date())