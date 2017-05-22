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

def about(request):
        contact = Contact.objects.first()
        about = About.objects.first()
        contenuto = Contenuto.objects.first() 
        return render(request,'about.html',{
                                'contact':contact,
                                 'about':about,
                                 'contenuto':contenuto,
                                 'page':'about'
                                 })    
                                 
def work(request):
        contact = Contact.objects.first()
        work = Work.objects.all()
        contenuto = Contenuto.objects.first() 
        return render(request,'work.html',{
                                'contact':contact,
                                'work':work,
                                'contenuto':contenuto,
                                'page':'work'
                                })

def contact(request):
        contact = Contact.objects.first()
        contenuto = Contenuto.objects.first() 
        return render(request,'contact.html',{
                                'contact':contact,
                                'contenuto':contenuto,
                                'page':'contact'
                                })

                                
def privacy(request):
        contact = Contact.objects.first()
        contenuto = Contenuto.objects.first() 
        return render(request,'privacy.html',{
                                'contact':contact,
                                'contenuto':contenuto,
                                'page':'contatti',
                                })