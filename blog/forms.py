from django import forms
from django.db import transaction

from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('nom','commentaire')

    def __init__(self, *args, **kwargs):
        super(CommentaireForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['commentaire'].widget.attrs.update({'class': 'form-control'})
      