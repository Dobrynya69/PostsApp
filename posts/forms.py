from django import forms
from .models import *

class SortForm(forms.Form):
    search = forms.CharField(max_length=250, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Post title'}))
    theme = forms.ModelChoiceField(Theme.objects, label='', required=False)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'themes']
    