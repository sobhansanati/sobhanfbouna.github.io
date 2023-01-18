from django.forms import * 
from django import forms
from . import models



class SenderForm(forms.ModelForm):
    class Meta:
        managed = True
        verbose_name = 'Email_sender'
        verbose_name_plural = 'Email_sender'
        model = models.Email_sender
        fields = ('Sender',)
        labels ={
            'Sender' : ""
        }
        
        
        widgets = {
            'Sender':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter the Email'}),
        }
