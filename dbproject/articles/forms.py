from django import  forms
import json
from .models import Articles, Category, ArticleTypes


class ArticlesForm(forms.ModelForm):
    categorys = Category.objects.all()
    types = ArticleTypes.objects.all()
    category_choices = []
    type_choices = []

    for c in categorys:
        category_choices.append((c.name, c.name))

    for t in types:
        type_choices.append((t.name, t.name))
    print(type_choices)

    name = forms.CharField(label="Name", max_length=100)
    category = forms.ChoiceField(label="Category", choices=category_choices)
    type = forms.ChoiceField(label="Type", choices=type_choices)
    about = forms.CharField(label="About", max_length=1500, widget=forms.Textarea)
    fields = forms.JSONField(label="Fields (JSON)", max_length=1000, widget=forms.Textarea)

    class Meta:
        model = Articles
        fields = '__all__'

class SearchForm(forms.ModelForm):
    search = forms.CharField()