from django.shortcuts import render
from home.models import *
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext, Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django import forms


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