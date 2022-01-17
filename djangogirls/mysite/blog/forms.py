from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # 폼을 만들기 위해 쓰여야 하는 model
        fields = ('title', 'text',)