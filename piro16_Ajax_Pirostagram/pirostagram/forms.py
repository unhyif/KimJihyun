from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["like"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["parent_post"]