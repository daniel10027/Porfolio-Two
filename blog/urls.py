
from django.contrib import admin
from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, Comment
urlpatterns = [
   
   path("articles/", ArticleListView.as_view(),name="articles"),
   path("article/details/<int:pk>&remeinder=<slug:slug>/", ArticleDetailView.as_view(),name="article-details"),
   path("commentaires/", Comment ,name="commentaires"),
    
]
