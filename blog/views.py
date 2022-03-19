from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from .models import CategorieArticle, Article, Commentaire
import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentaireForm
from django.db.models import Q


class ArticleListView(ListView):

    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
  
    def get_queryset(self): # new
        query = int(self.request.GET.get('q'))
        object_list = Article.objects.filter(
            Q(categorie=query) 
        )
        
        return object_list.order_by('-created')

    def get_context_data(self, **kwargs):
            context = super(ArticleListView, self).get_context_data(**kwargs)
            return context

class  ArticleDetailView(DetailView):
    model = Article
    template_name = "blog-single.html"
    pk_url_kwarg = "article_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
 
    def get_object(self, *args, **kwargs):

        request = self.request
        slug = self.kwargs.get('slug')
        pk = self.kwargs.get('pk')

        try:

          instance = Article.objects.get(slug=slug, active=True, pk=pk)

        except Article.DoesNotExist: 

            raise Http404("Cet   produit n'existe pas !")

        except Article.MultipleObjectsReturned:

            qs = Article.objects.filter(slug=slug, active=True, pk=pk)

            instance =  qs.first()

        except:

            raise Http404("Ce  produit n'existe pas !")

        return instance

    def get_context_data(self, **kwargs):
            context = super(ArticleDetailView, self).get_context_data(**kwargs)
            context['categories'] = CategorieArticle.objects.all()
            context['trois'] = Article.objects.all()[:3]
            context['state'] = True
            return context
        
    def post(self, request, *args, **kwargs):
        
        form = CommentaireForm(request.POST)
        
        if form.is_valid():
          
            reply = form.save(commit=False)
            reply.article = self.get_object()
            reply.save()
            self.object = self.get_object()
            context = context = super().get_context_data(**kwargs)
            context['form'] = CommentaireForm
            context['message'] = "Commentaire ajouté"
            context['categories'] = CategorieArticle.objects.all()
            context['trois'] = Article.objects.all()[:3]
            context['state'] = True
            

            return self.render_to_response(context=context)

        else:
          
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = CommentaireForm
            context['categories'] = CategorieArticle.objects.all()
            context['trois'] = Article.objects.all()[:3]
            context['state'] = True

            return self.render_to_response(context=context)


    