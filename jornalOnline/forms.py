from django import forms
from .models import Article, Comment, Rating

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'category']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
