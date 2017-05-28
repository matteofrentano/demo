"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home import views as view_home
from about import views as view_about
from work import views as view_work
from contact import views as view_contact
from django.conf.urls import include, url


urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', view_home.home, name='home'),
        url(r'^home/', view_home.home, name='home'),
        url(r'^about/$', view_about.about,name="about"),   
        url(r'^work/$',view_work.work,name="work"), 
        url(r'^contact/$', view_contact.contact, name="contact"), 
        url(r'^privacy/$',view_contact.privacy,name="privacy"),
        #url(r'^email/$', view_contact.email, name='email'),
        #url(r'^thanks/$', view_contact.thanks, name='thanks'),
        


        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
