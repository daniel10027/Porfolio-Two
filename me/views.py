from django.shortcuts import render, redirect
from .models import *
from blog.models import CategorieArticle, Article
from django.http import Http404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect





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

def Contact(request):

    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form, "ms":False }
    else:
        
        form = ContactForm(request.POST)
        context = { 'form': form, "ms":True }
        if form.is_valid():
            nom = form.cleaned_data['nom']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            objet = form.cleaned_data['objet']
            message = form.cleaned_data['message']
            s_email = Me.objects.last()
            sujet = 'Message de ' + nom + ' Contact : ' + contact + ' Email : ' + email + ' Objet : ' + objet
            try:
                send_mail(sujet, message, s_email.email_1 , [s_email.email_1])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Merci votre méssage a bien été envoyé .\n Nous vous recontacterons dans les plus bref délais" )
            return redirect('home')
        
        
