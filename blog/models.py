from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class CategorieArticle(models.Model):
    """Model definition for CategorieArticle."""
    titre = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for CategorieArticle."""

        verbose_name = 'CategorieArticle'
        verbose_name_plural = 'CategorieArticles'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of CategorieArticle."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for CategorieArticle."""
        return ('')
    
    @property
    def articles(self):
        return self.categories.all()
    
    @property
    def article(self):
        return self.articles.count()
    
    

    # TODO: Define custom methods here
    
class Article(models.Model):
    """Model definition for Articles."""
    
    categorie = models.ForeignKey(CategorieArticle, related_name='categories',on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    base = models.TextField(blank=True, null=True)
    description = HTMLField()
    section_1 = HTMLField()
    image_2 = models.CharField(max_length=150)
    section_2 = HTMLField()
    section_3 = HTMLField()
    accroche = HTMLField()
    slug = AutoSlugField(populate_from='titre')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Articles."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Articles."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for Articles."""
        return ('')
    
    @property
    def comments(self):
        return self.commentaires.all().order_by('-created')
    
    def url(self):
        return reverse("article-details", 
        kwargs={

            "slug": self.slug, 
            "pk": self.pk,
         
            
            })
    # TODO: Define custom methods here


class Commentaire(models.Model):
    """Model definition for Commentaire."""
    article = models.ForeignKey(Article, related_name='commentaires',on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    commentaire = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.article.titre

  
    def get_absolute_url(self):
        """Return absolute url for Commentaire."""
        return ('')

    # TODO: Define custom methods here
