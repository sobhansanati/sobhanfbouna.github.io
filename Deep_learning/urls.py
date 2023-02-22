from django.urls import path
from . import views



app_name = 'Home'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('Deeplearning/',views.Deep_learning,name='Dl'),
]
