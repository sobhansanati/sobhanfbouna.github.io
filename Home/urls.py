from django.urls import path
#from .views import AddEmail
from . import views

app_name = 'Home'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('',views.email_sender,name='email_sender'),
    path('homepage/',views.Homepage,name='Home_H'),
]