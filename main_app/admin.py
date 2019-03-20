from django.contrib import admin
from .models import Record, Track, Artist, Photo

# Register your models here.
admin.site.register(Record)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Photo)