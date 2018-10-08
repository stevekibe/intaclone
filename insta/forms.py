from .models import Profile
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['pub_date']
        