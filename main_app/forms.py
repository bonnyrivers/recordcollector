from django.forms import ModelForm
from django import forms
from .models import Track, Artist
from main_app.genres import *

class TrackForm(ModelForm):
  class Meta:
    model = Track
    fields = ['track_num', 'title']

class ArtistForm(ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'genre']