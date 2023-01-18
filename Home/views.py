from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import ListView , DetailView , CreateView
from .forms import SenderForm


def email_sender(request):
    if request.method == "POST":
        form = SenderForm(request.POST)
        if form.is_valid():
            form.save()
            form2 = SenderForm()
            return render(request,'Home/signup.html',{'form':form2})
    else:
        form = SenderForm()
    return render(request,'Home/signup.html',{'form':form})
            
def Homepage(request):
    return render(request,'Home/Homepage.html')