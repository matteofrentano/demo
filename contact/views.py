from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from home.models import *
from django.contrib import messages
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext, Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django import forms
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError




def contact(request):
        contact = Contact.objects.first()
        contenuto = Contenuto.objects.first() 
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['nome']
                from_email = form.cleaned_data['email']
                message = form.cleaned_data['messaggio']
                try:
                    send_mail(subject, message, from_email, ['matteocarabba@gmail.com'], fail_silently=False,)
                except BadHeaderError:
                    return HttpResponse('Ci spiace, deve esserci stato un errore')             
        return render(request,  'contact.html',{
                                'contact':contact,
                                'contenuto':contenuto,
                                'page':'contact',
                                'form' : ContactForm()
                                })

                                
def privacy(request):
        contact = Contact.objects.first()
        contenuto = Contenuto.objects.first() 
        return render(request,'privacy.html',{
                                'contact':contact,
                                'contenuto':contenuto,
                                'page':'contatti',
                                })














