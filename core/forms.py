from django import forms
from django.contrib.auth.models import User
from .models import AnimalProfile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

