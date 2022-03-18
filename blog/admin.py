from django.contrib import admin
from .models import *

class ArticleAdmin(admin.TabularInline):
    model = Article
    extra = 0
    

class CommentaireInline(admin.TabularInline):
    model = Commentaire
    extra = 0
    
    
@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    search_fields = ['article__titre', 'nom']
    list_display = ('article','nom', 'active', 'created', 'date_update', )
    
    



@admin.register(CategorieArticle)
class MeAdmin(admin.ModelAdmin):
    search_fields = ['titre']
    inlines = [ArticleAdmin,]
    list_display = ('titre','article', 'active', 'created', 'date_update', )
    
    

@admin.register(Article)
class MeAdmin(admin.ModelAdmin):
    inlines = [CommentaireInline,]
    search_fields = ['titre']
    list_display = ('titre', 'active', 'created', 'date_update', )
    
    