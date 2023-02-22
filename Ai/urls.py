from django.urls import path
from . import views



app_name = 'Ai'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('Ai/',views.Ai,name='AI'),
]
