from django import forms
from .models import Category, Tutorial

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent']

class TutorialCreateForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'text', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control m-2'

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'category_type', 'text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = False

    #text = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
