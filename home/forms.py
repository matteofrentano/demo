from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_ragione_sociale = forms.CharField(required=False)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Il tuo nome:"
        self.fields['contact_email'].label = "La tua email:"
        self.fields['content'].label = "Il tuo messaggio:"