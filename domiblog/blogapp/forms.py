from django import forms
from .models import Post, Category

# categories = [('coding', 'coding'), ('travels', 'travels'),
#               ('health', 'health'), ('sports', 'sports'), ('people', 'people'), ]

categories = Category.objects.all().values_list('name', 'name')
categories_list = []

for category in categories:
    categories_list.append(category)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'preview', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'post_author', 'type': 'hidden'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'preview': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'preview')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'preview': forms.Textarea(attrs={'class': 'form-control'}),
        }
