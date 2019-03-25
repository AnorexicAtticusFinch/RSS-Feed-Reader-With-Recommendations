from .models import Source
from django import forms
 
class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['link','file_name']
