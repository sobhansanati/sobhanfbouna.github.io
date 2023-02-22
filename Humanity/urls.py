from django.urls import path
from . import views


app_name = 'Humanity'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('Philosophy/',views.philo,name='Philosophy_1'),
    path('sociolgy/',views.soc,name='socio')
]
