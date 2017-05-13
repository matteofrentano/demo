from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext

def home(request):
        slide = Slide.objects.all()
        contenuto = Contenuto.objects.first()    
        return render_to_response('index.html',
                             {
                             'slide':slide,
                              'contenuto':contenuto,
                              'page':'home',
                              },
                             RequestContext(request))                            

def about(request):
        about = About.objects.first()
        contenuto = Contenuto.objects.first() 
        return render(request,'about.html',{
                                 'about':about,
                                 'contenuto':contenuto,
                                 'page':'about'
                                 })    
                                 
def work(request):
        work = Work.objects.all()
        contenuto = Contenuto.objects.first() 
        return render(request,'work.html',{
                                'work':work,
                                'contenuto':contenuto,
                                'page':'work'
                                })
    
def contact(request):
        contenuto = Contenuto.objects.first() 
        return render(request,'contact.html',{
                                'page':'contact',
                                'contenuto':contenuto,
                                })