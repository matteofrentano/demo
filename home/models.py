from django.db import models

class Contenuto(models.Model):      
    titolo_home = models.TextField(max_length=100, blank=True,)
    sottotitolo_home = models.TextField(max_length=100, blank=True,)
    testo_home = models.TextField(max_length=3000, blank=True,)
    immagine_box_1 = models.FileField(max_length=500,blank=True,)
    testo_box_1 = models.TextField(max_length=3000, blank=True,)
    immagine_box_2 = models.FileField(max_length=500,blank=True,)
    testo_box_2 = models.TextField(max_length=3000, blank=True,)
    immagine_box_3 = models.FileField(max_length=500,blank=True,)
    testo_box_3 = models.TextField(max_length=3000, blank=True,)
    immagine_box_4 = models.FileField(max_length=500,blank=True,)
    testo_box_4 = models.TextField(max_length=3000, blank=True,)   
    
    sottotesto_home = models.TextField(max_length=3000, blank=True,)
    try:        
        testo_footer= RichTextField(max_length=100000,blank=True,)
    except:
        testo_footer= models.TextField(blank=True,)
    class Meta:
        verbose_name="Home"
        verbose_name_plural="Modifica il contenuto della Home"
        
    def __unicode__(self):
        return u"Modifica il contenuto della Home"   
    
                        
                        
class Slide(models.Model):
    immagine = models.FileField(max_length=500)
    titolo = models.CharField(max_length=100,blank=True)      
    attivo = models.BooleanField(default=True)  
    class Meta:
        verbose_name="Slide"
        verbose_name_plural="Modifica le immagini della Slide"
        
    def __unicode__(self):
        return u"%d - %s" % (self.id,self.titolo)
    
    def admin_thumbnail(self):
        return u'<img style="max-width:150px" src="%s" />' % (self.immagine.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    
class About(models.Model):   
    immagine_box_1 = models.FileField(max_length=500,blank=True,)
    immagine_box_2 = models.FileField(max_length=500,blank=True,)
    immagine_box_3 = models.FileField(max_length=500,blank=True,)
    immagine_box_4 = models.FileField(max_length=500,blank=True,)
    titolo_about = models.TextField(max_length=100, blank=True,)
    testo_about = models.TextField(max_length=3000, blank=True,)
    class Meta:
        verbose_name="About"
        verbose_name_plural="Modifica il contenuto della pagina About"
        
    def __unicode__(self):
        return u"Modifica il contenuto della pagina About"
        
class Work(models.Model):   
    screen = models.FileField(max_length=500,blank=True,)
    logo = models.FileField(max_length=500,blank=True,)    
    titolo_work = models.TextField(max_length=100, blank=True,)
    descrizione_work = models.TextField(max_length=3000, blank=True,)
    class Meta:
        verbose_name="Work"
        verbose_name_plural="Modifica il contenuto della pagina Work"
        
    def __unicode__(self):
        return u"Modifica il contenuto della pagina Work"
        
        
        
        
        
        
        