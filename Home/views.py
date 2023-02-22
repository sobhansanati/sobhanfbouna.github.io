from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.generic import ListView , DetailView , CreateView
from .forms import SenderForm
from django.core.mail import EmailMessage


def Conatactpage(request):
        return render(request,'Home/cntc.html')

            
def Homepage(request):
    Form = SenderForm(request.POST)
    return render(request,'Home/homepage.html',{'Form':Form})

def contactform(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'])
        send_mail('You got a mail!', message, '', ['<contact@sobhanfbouna.com>']) # TODO: enter your email address
        
    return render(request, 'Home/homepage.html', {})