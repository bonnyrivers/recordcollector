from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Record

def home(request):
    return render(request, 'about.html')
    
def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})

def records_details(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/details.html', {'record': record})

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
