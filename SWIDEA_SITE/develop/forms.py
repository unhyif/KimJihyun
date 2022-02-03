from django import forms
from .models import *

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = "__all__"

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = "__all__"
