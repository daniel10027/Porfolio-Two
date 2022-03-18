from django.contrib import admin
from .models import *
# Register your models here.


class ProjetInline(admin.TabularInline):
    model = Projet
    extra = 0
    


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom']
    list_display = ('nom', 'prenom', 'date_de_naissance', 'telephone_1', 'telephone_2',  'active', 'created', 'date_update', )
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    list_display = ('titre' ,'active', 'created', 'date_update', )
    
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    search_fields = ['activite']
    list_display = ('activite' ,'active', 'created', 'date_update', )
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    list_display = ('titre' ,'active', 'created', 'date_update', )
    
    
@admin.register(CategorieProjet)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    inlines = [ProjetInline,]
    list_display = ('titre' ,'active', 'created', 'date_update', )
    
    
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    list_display = ('titre' ,'active', 'created', 'date_update', )