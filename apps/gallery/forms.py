from django import forms
from .models import Photography


class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['published', 'created_at', 'updated_at', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'image': 'Imagem',
            'published': 'Publicado',
        }
