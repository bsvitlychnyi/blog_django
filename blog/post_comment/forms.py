from django import forms
from .models import Comment, Post


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets ={
        	'title': forms.TextInput(attrs={'class': 'form-control'}),
        	'body': forms.Textarea(attrs={'class': 'form-control', 'rows':"2"}),
        	}

        labels = {
            'title': 'Заголовок поста',
            'body': 'Основной текст поста',
        }