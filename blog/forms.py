from django import forms
from . import models
from .models import Comment, Message


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'reciever']