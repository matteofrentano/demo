from django.shortcuts import render
from .models import *
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext

def home(request):
    
    contenuto = Contenuto.objects.first()
    foto = None
    
    return render_to_response('index.html',
                             {
                              'contenuto':contenuto,
                              'gallery':foto,
                              'page':'home',
                              },
                             RequestContext(request))
                             
def about(request):
    return render(request,'about.html',{'page':'about'})
    
def work(request):
    return render(request,'work.html',{'page':'work'})
    
def contact(request):
    return render(request,'contact.html',{'page':'contact'})