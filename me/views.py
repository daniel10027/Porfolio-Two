from django.shortcuts import render
from .models import *
from blog.models import CategorieArticle, Article

# Create your views here.
def Home(request):
    context = { 
               
            'me':Me.objects.last(),
            "services" : Service.objects.all(),
            "competances" : Competence.objects.all(),
            "educations": Education.objects.all(),
            "categorie_projet": CategorieProjet.objects.all(),
            "projets": Projet.objects.all(),
            "articles": Article.objects.all()[:2]
           
               }
    return render(request, 'index.html', context)