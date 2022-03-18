from django.db import models
import datetime

# Create your models here.
class Me(models.Model):
    """Model definition for Me."""
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    poste = models.CharField(max_length=150, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_de_naissance = models.DateField()
    telephone_1 = models.CharField(max_length=10, blank=True, null=True)
    telephone_2 = models.CharField(max_length=10, blank=True, null=True)
    annee = models.IntegerField()
    email_1 = models.EmailField(blank=True, null=True)
    email_2 = models.EmailField(blank=True, null=True)
    localite = models.CharField(max_length=50, blank=True, null=True)
    freelance = models.CharField(max_length=50, blank=True, null=True)
    lien_cv = models.CharField(max_length=150)
    lien_photo = models.CharField(max_length=150)
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Me."""

        verbose_name = 'Me'
        verbose_name_plural = 'Mes'

    def __str__(self):
        """Unicode representation of Me."""
        return '{} {}'.format(self.nom, self.prenom)
    
    @property
    def cv(self):
        return 'https://drive.google.com/uc?export=view&id={}'.format(self.lien_cv)
    
    @property
    def photo(self):
        return 'https://drive.google.com/uc?export=view&id={}'.format(self.lien_photo)
    
    @property
    def age(self):
        return datetime.date.today().year -self.date_de_naissance.year

    

    # TODO: Define custom methods here

class Service(models.Model):
    """Model definition for Service."""
    icon = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for Service."""
        return ('')

    # TODO: Define custom methods here


class Competence(models.Model):
    """Model definition for Competence."""
    activite = models.CharField(max_length=50)
    niveau = models.IntegerField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Competence."""

        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Competence."""
        return self.activite


    def get_absolute_url(self):
        """Return absolute url for Competence."""
        return ('')

    # TODO: Define custom methods here


class Education(models.Model):
    """Model definition for Education."""
    titre = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Education."""

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Education."""
        return self.titre


    def get_absolute_url(self):
        """Return absolute url for Education."""
        return ('')

    # TODO: Define custom methods here


class CategorieProjet(models.Model):
    
    titre = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    """Model definition for CategorieProjet."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for CategorieProjet."""

        verbose_name = 'CategorieProjet'
        verbose_name_plural = 'CategorieProjets'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of CategorieProjet."""
        return self.titre

  

    def get_absolute_url(self):
        """Return absolute url for CategorieProjet."""
        return ('')

    # TODO: Define custom methods here
    
    
class Projet(models.Model):
    """Model definition for Projet."""
    categorie = models.ForeignKey(CategorieProjet, related_name="projets", on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    description = models.TextField()
    lien = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Projet."""

        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
        ordering = ['-created']

    def __str__(self):
        """Unicode representation of Projet."""
        return self.titre


    def get_absolute_url(self):
        """Return absolute url for Projet."""
        return ('')

    @property
    def images(self):
        return 'https://drive.google.com/uc?export=view&id={}'.format(self.image)
    # TODO: Define custom methods here

