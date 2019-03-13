from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Artist
from .forms import TrackForm

def home(request):
    return render(request, 'about.html')
    
def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
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

def assoc_artist(request, record_id, artist_id):
  # Note that you can pass a toy's id instead of the whole object
  Record.objects.get(id=record_id).artists.add(artist_id)
  return redirect('details', record_id=record_id)

def add_track(request, record_id):
    form = TrackForm(request.POST)
    if form.is_valid():
        new_track = form.save(commit=False)
        new_track.record_id = record_id
        new_track.save()
    return redirect('details', record_id=record_id)

class RecordCreate(CreateView):
    model = Record
    fields = '__all__'
    success_url = '/records/'

class RecordUpdate(UpdateView):
    model = Record
    fields = ['name', 'cover', 'artist', 'year', 'num_tracks']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

# views as classes

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'
    success_url = '/artists/'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = '__all__'

class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artists/'

