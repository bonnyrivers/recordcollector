from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover = models.CharField(max_length=200, default='images/record-logo.png')
    num_tracks = models.IntegerField()
    duration = models.IntegerField()
    year = models.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2020)])
    def __str__(self):
        return self.name + ' by ' + self.artist
