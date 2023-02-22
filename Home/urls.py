from django.urls import path
#from .views import AddEmail
from . import views

app_name = 'Home'
urlpatterns = [
    #path('',AddEmail.as_view(),name='Home'),
    path('ContactForm/',views.Conatactpage,name='contact_page'),
    path('',views.Homepage,name='Home_p'),
]
