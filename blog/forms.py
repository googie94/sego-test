from django import forms
from django.forms import Textarea
from .models import Post, Comment

class PostForm(forms.ModelForm):
	author=forms.CharField(widget=forms.TextInput(attrs={'class': 'inputFull mb10',}))
	title=forms.CharField(widget=forms.TextInput(attrs={'class': 'inputFull mb10',}))
	text=forms.CharField(widget=forms.Textarea(attrs={'class': 'inputFull height250 mb10',}))
    
	class Meta:
		model = Post
		fields = ('author', 'title', 'text')



class CommentForm(forms.ModelForm):
	text=forms.CharField(widget=forms.Textarea(attrs={'class': 'inputFull height250 mb10',}))

	class Meta:
		model = Comment
		fields = ('text',)