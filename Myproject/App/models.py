from django.db import models
from django.utils import timezone
# Create your models here.
class ClassVarity(models.Model):
    USERS =[
        ('AS', 'ASPIRANT'),
        ('RT', 'RECRUITER'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=2, choices = USERS)

def __str__(self):
    return self.name

