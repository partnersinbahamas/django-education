from django import forms
from .models import Article
# regular expration
import re
from django.core.exceptions import ValidationError

# This form conntected with Model (Article) and we can use then save() func
class ArticleForm(forms.ModelForm):
    class Meta:
        # here we bind form with model
        model = Article

        # we can use as well fields ='__all__', it took all fields from model
        fields = ['title', 'content', 'is_published', 'image', 'category']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
    
    """
    this is a custom validator for title field
    custom validator needs to start with clean_[fieldName]
    """
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if re.match(r'\d', title):
            raise ValidationError("Title can not start with number(s)")
        else:
            return title


# Alternative example to render a form with widgets
# This form isnt connected with Article model
"""
class ArticleForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    created_at = forms.DateTimeField(
        label='Date',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    is_published = forms.BooleanField(
        label='Publish',
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        # with empty_label=None will be selected first category in list
        empty_label="Select category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
"""