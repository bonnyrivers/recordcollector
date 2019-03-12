from django.urls import path
from . import views

# the routes will be defined here
urlpatterns = [
    # empty string is root path
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for records index
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_details, name='details'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    # update
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    #delete
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
]