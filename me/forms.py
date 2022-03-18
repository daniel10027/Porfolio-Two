from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    contact = forms.CharField(required=True)
    objet = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)