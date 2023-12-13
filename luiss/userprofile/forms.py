from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'Twitter',
            'Facebook',
            'Instagram',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model= User
        fields= ['username', 'email']


