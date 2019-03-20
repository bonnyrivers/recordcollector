from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Artist
from .forms import TrackForm
from .genres import *
import uuid
import boto3
from .models import Record, Artist, Photo, Track
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'recordcollector'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # How to create a user form object w/browser data
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # a bad post or get req render signup.html empty
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Record Classes and fns

class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record
    fields = '__all__'
    success_url = '/records/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecordUpdate(LoginRequiredMixin, UpdateView):
    model = Record
    fields = ['name', 'cover', 'artist', 'year', 'num_tracks']

class RecordDelete(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = '/records/'

# Login required for personalized pages

@login_required
def records_index(request):
    records = Record.objects.filter(user = request.user)
    return render(request, 'records/index.html', {'records': records})

def records_details(request, record_id):
    record = Record.objects.get(id=record_id)
    artists_not_featured = Artist.objects.exclude(id__in = record.artists.all().values_list('id'))
    track_form = TrackForm()
    return render(request, 'records/details.html', {
        'record': record,
        'track_form': track_form,
        'artists': artists_not_featured
    })

@login_required
def add_track(request, record_id):
    form = TrackForm(request.POST)
    if form.is_valid():
        new_track = form.save(commit=False)
        new_track.record_id = record_id
        new_track.save()
    return redirect('details', record_id=record_id)

@login_required
def add_photo(request, record_id):
	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, record_id=record_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', record_id=record_id)

# Artist Classes

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    genres = GENRES
    fields = '__all__'
    success_url = '/artists/'

class ArtistUpdate(LoginRequiredMixin, UpdateView):
    model = Artist
    fields = '__all__'

class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = '/artists/'

@login_required
def assoc_artist(request, record_id, artist_id):
  # Note that you can pass a toy's id instead of the whole object
  Record.objects.get(id=record_id).artists.add(artist_id)
  return redirect('details', record_id=record_id)

def home(request):
    return render(request, 'about.html')
    
def about(request):
    return render(request, 'about.html')

