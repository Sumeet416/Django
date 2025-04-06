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

class Reviews(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    chai_varity = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.chai_varity.name}'
    
