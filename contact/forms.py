from django import forms

class ContactForm(forms.Form):

    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=100, required=True)
    messaggio = forms.CharField(widget=forms.Textarea)