from django import forms
from django.forms import ModelForm
from .models import PostForm

class PostForm(forms.ModelForm): 
    description = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={"rows":5, "cols":20}
        ),)   
    quantity = forms.IntegerField(required=True)