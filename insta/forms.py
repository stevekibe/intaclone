from .models import Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Profile
        