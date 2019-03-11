from django.shortcuts import render
from django.http import HttpResponse
from .models import Record


# class Record:
#     def __init__(self, name, artist, num_tracks, duration, year):
#         self.name = name
#         self.artist = artist
#         self.num_tracks = num_tracks
#         self.duration = duration
#         self.year = year

# records = [
#     Record("Mama's Gun", 'Erykah Badu', 14, 71, 2000),
#     Record("Sound Of Silver", 'LCD Soundsystem', 9, 56, 2007),
#     Record("The Life Of Pablo", 'Kanye West', 14, 59, 2000),
#     Record("Hyperion", 'Gesaffelstein', 10, 40, 2019),
#     Record("While We Wait", 'Kehlani', 9, 31, 2019),
#     Record("Small Black EP", 'Small Black', 7, 27, 2009),
# ]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello and welcome to RecordCollector</h1>')
    
def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})

def records_details(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/details.html', {'record': record})