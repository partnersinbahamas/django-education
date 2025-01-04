from django import forms
from .models import Category

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.TextInput()
    created_at = forms.DateTimeField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())