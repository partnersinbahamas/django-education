from django import forms
from .models import Category

# This form isnt connected with Article model
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

    # Alternative example to render a form with widgets
    # This form conntected with Model (Article) and we can use then save() func
    """
    class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desctiption', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Name',
            }),
            'desctiption': TextInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Desctiption',
            }),
            'text': Textarea(attrs={
                'class': 'form_item form-control',
                'placeholder': 'State',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form_item form-control',
                'placeholder': 'Date',
                'type': 'date'
            }),
        }
    """