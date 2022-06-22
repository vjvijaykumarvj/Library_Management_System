from .models import library_Model
from django import forms

class library_Forms(forms.ModelForm): #Model+Forms = ModelForms
    class Meta:
        fields = '__all__'
        model = library_Model