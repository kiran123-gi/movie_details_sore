from django import forms
from .models import movies
class moviesForms(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['sno','name','hero','heroine','director','music','year']