from django.contrib import admin
from .models import *

class ContenutoAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        base_add_permission = super(ContenutoAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = Contenuto.objects.all().count()
            if count == 0:
                return True
        return False

admin.site.register(Contenuto,ContenutoAdmin)

class SlideAdmin(admin.ModelAdmin):
    save_on_top = True    
    list_display=['titolo','admin_thumbnail','attivo']
    
admin.site.register(Slide,SlideAdmin)

class AboutAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        base_add_permission = super(AboutAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            count = About.objects.all().count()
            if count == 0:
                return True
        return False

admin.site.register(About,AboutAdmin)

class WorkAdmin(admin.ModelAdmin):
    save_on_top = True
    

admin.site.register(Work,WorkAdmin)