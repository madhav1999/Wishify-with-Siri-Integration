from logging import NOTSET
from socket import fromshare
from django import forms
from django.core.exceptions import ValidationError

from .models import forTwi

class forTwiForm(forms.ModelForm):
    class Meta:
        model = forTwi
        fields = ('link', 'description')
        widgets={
            'link': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'description': forms.Textarea(attrs={"class":"form-control mb5"})
        }

    def clean_link(self):
        link = self.cleaned_data['link']
        if 'https://www.twitter.com' not in link:
            raise ValidationError('enter only twitter links')
        return link
    
    