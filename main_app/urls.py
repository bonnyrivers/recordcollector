from django.urls import path
from . import views

# the routes will be defined here
urlpatterns = [
    # empty string is root path
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('records/', views.records_index, name='index')
]

