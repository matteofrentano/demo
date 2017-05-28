from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext, Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django import forms



def home(request):
        slide = Slide.objects.all()
        contenuto = Contenuto.objects.first()    
        contact = Contact.objects.first()
        return render_to_response('index.html',
                             {
                             'contact':contact,
                             'slide':slide,
                              'contenuto':contenuto,
                              'page':'home',
                              },
                             RequestContext(request))                            
                                 


