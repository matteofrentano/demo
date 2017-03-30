from django.db import models

class Contenuto(models.Model):   
    try:        
        testo_footer= RichTextField(max_length=100000,blank=True,)
    except:
        testo_footer= models.TextField(blank=True,)
    immagine_box_1 = models.FileField(max_length=500,blank=True,)
    immagine_box_2 = models.FileField(max_length=500,blank=True,)
    immagine_box_3 = models.FileField(max_length=500,blank=True,)
    immagine_box_4 = models.FileField(max_length=500,blank=True,)
    cambia_automaticamente_gallery = models.BooleanField(default=False)
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