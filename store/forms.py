from django import forms
from store.models import Contact

class Contactform(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"