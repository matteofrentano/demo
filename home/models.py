from django.db import models

class Contenuto(models.Model):      
    titolo_home = models.TextField(max_length=100, blank=True,)
    sottotitolo_home = models.TextField(max_length=100, blank=True,)
    testo_home = models.TextField(max_length=3000, blank=True,)   
    sottotesto_home = models.TextField(max_length=3000, blank=True,)
    link_fb = models.CharField(max_length=100, blank=True,)
    link_tw = models.CharField(max_length=100, blank=True,)
    link_yt = models.CharField(max_length=100, blank=True,)
    link_ig = models.CharField(max_length=100, blank=True,)
    link_lk = models.CharField(max_length=100, blank=True,)
    link_gp = models.CharField(max_length=100, blank=True,)
    try:        
        testo_footer= RichTextField(max_length=100000,blank=True,)
    except:
        testo_footer= models.TextField(blank=True,)
    class Meta:
        verbose_name="Home"
        verbose_name_plural="Modifica il contenuto della Home"
        
    def __str__(self):
        return 'Contenuto'
  
    
                        
                        
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
    titolo_about = models.TextField(max_length=100, blank=True,)
    testo_about = models.TextField(max_length=3000, blank=True,)
    immagine_box_1 = models.FileField(max_length=500,blank=True,)
    testo_box_1 = models.TextField(max_length=3000, blank=True,)
    immagine_box_2 = models.FileField(max_length=500,blank=True,)
    testo_box_2 = models.TextField(max_length=3000, blank=True,)
    immagine_box_3 = models.FileField(max_length=500,blank=True,)
    testo_box_3 = models.TextField(max_length=3000, blank=True,)
    immagine_box_4 = models.FileField(max_length=500,blank=True,)
    testo_box_4 = models.TextField(max_length=3000, blank=True,) 
    immagine_box_5 = models.FileField(max_length=500,blank=True,)
    testo_box_5 = models.TextField(max_length=3000, blank=True,)       
    class Meta:
        verbose_name="About"
        verbose_name_plural="Modifica il contenuto della pagina About"
        
    def __str__(self):
        return 'About'
        
class Work(models.Model):   
    screen = models.FileField(max_length=500,blank=True,)   
    titolo_work = models.TextField(max_length=100, blank=True,)
    descrizione_work = models.TextField(max_length=3000, blank=True,)
    link = models.URLField(max_length=200, blank=True,)
    class Meta:
        verbose_name="Work"
        verbose_name_plural="Modifica il contenuto della pagina Work"
        
    def __str__(self):
        return self.titolo_work
        
        
class Contact(models.Model):   
    nome_azienda = models.CharField(max_length=100, blank=True,)
    indirizzo_azienda = models.CharField(max_length=100, blank=True,)
    civico_azienda = models.CharField(max_length=100, blank=True,)
    cap = models.CharField(max_length=5, blank=True,)
    comune = models.CharField(max_length=100, blank=True,)
    provincia = models.CharField(max_length=100, blank=True,)
    tel = models.CharField(max_length=30, blank=True,)
    email = models.EmailField(blank=True,)
    p_iva = models.CharField(max_length=14,blank=True,)
    numero_rea = models.CharField(max_length=14,blank=True,)
    pec = models.EmailField(blank=True,)
    
    class Meta:
        verbose_name="Contatti"
        verbose_name_plural="Modifica i dati di contatto"
        
    def __str__(self):
        return 'Contatti'
        
        
        
        