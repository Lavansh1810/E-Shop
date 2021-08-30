from django.contrib import admin

from .models import *

class KitchenAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Kitchen,KitchenAdmin)

class ClothingAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Clothing,ClothingAdmin)

class ShoesAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Shoes,ShoesAdmin)

class ElectronicsAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Electronics,ElectronicsAdmin)

class GymAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Gym,GymAdmin)

class Daily_UseAdmin(admin.ModelAdmin):
    list_display=('name','is_published','is_hot')
    list_display_links=('name',)
    
    list_editable=('is_published','is_hot')
    
    list_per_page=25
 
admin.site.register(Daliy_Use,Daily_UseAdmin)

