from django import forms
from playground.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        widgets = {'title': forms.TextInput(attrs = {'class':'form-control'}),
                   'content': forms.TextInput(attrs={'class':'form-control'}),
                   'image': forms.URLInput(attrs={'class': 'form-control'}),
                   }