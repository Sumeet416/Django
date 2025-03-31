from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    ALL_CHAI_VARITY = [
        ('GN', 'GINGER'),
        ('ML', 'MASALA'),
        ('GN', 'GREEN'),
        ('HB', 'HERBAL'),
        ('LN', 'LEMON'),
        ]
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='images/')
    type = models.CharField(max_length=2, choices=ALL_CHAI_VARITY)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
