from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.urls import reverse
from main_app.genres import *
from django.contrib.auth.models import User

GENRES = (
    ('ALT', 'Alternative'),
    ('AMB', 'Ambient'),
    ('BLU', 'Blues'),
    ('CLA', 'Classical'),
    ('DIS', 'Disco'),
    ('EMO', 'Emo'),
    ('EXP', 'Experimental'),
    ('FOL', 'Folk'),
    ('FUN', 'Funk'),
    ('HOU', 'House'),
    ('IDT', 'Industrial'),
    ('IND', 'Indie'),
    ('MET', 'Metal'),
    ('PUN', 'Punk'),
    ('RAP', 'Rap'),
    ('REG', 'Reggae'),
    ('SKA', 'Ska'),
    ('SOT', 'Soundtrack'),
    ('SOU', 'Soul'),
    ('TEC', 'Techno'),
)

class Artist(models.Model):
    name = models.CharField('name', max_length=100)
    genre = models.CharField(
        max_length=20,
        choices=GENRES,
        default=GENRES[0][0]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artists_detail', kwargs={'pk': self.id})

# Create your models here.
class Record(models.Model):
    name = models.CharField('album name', max_length=100)
    artist = models.CharField(max_length=100)
    cover = models.CharField('Cover Image URL', max_length=200, default='images/record-logo.png')
    num_tracks = models.IntegerField()
    duration = models.IntegerField()
    year = models.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2020)])
    artists = models.ManyToManyField(Artist)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name + ' by ' + self.artist

    def get_absolute_url(self):
        return reverse('details', kwargs={'record_id': self.id})


class Track(models.Model):
    title = models.CharField('track title', max_length=100)
    track_num = models.IntegerField('track number')

    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.track_num}. {self.title}"
    
    class Meta:
        ordering = ['track_num']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for record_id: {self.record_id} @{self.url}"