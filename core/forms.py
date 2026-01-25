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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Luna'}),
            'species': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wolf'}),
            'gender': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 4'}),
            'energy_level': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'social_style': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'bonding_style': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'preference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Strong companion'}),
        }
    
    # Explicitly defining image to make it required (model has it as optional)
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'd-none', 'id': 'id_image', 'onchange': 'previewImage(this)'}))

    # Add extra choices for free-text fields to allow "Chip" selection
    ACTIVITY_CHOICES = [('Day', 'Day'), ('Night', 'Night'), ('Any', 'Any')]
    activity_cycle = forms.ChoiceField(choices=ACTIVITY_CHOICES, widget=forms.RadioSelect(attrs={'class': 'btn-check'}))
    
    # Hide others or give defaults? Let's keep them hidden/default for now to simplify
    # We will handle these defaults in the view if not present, or just render them hidden with JS defaults
    habitat = forms.CharField(widget=forms.HiddenInput(), initial="Unknown")
    territory = forms.CharField(widget=forms.HiddenInput(), initial="Unknown")
    personality = forms.CharField(widget=forms.HiddenInput(), initial="Friendly")
    diet = forms.CharField(widget=forms.HiddenInput(), initial="Omnivore")
    preference = forms.CharField(widget=forms.HiddenInput(), initial="To be loved")
    favorite_activity = forms.CharField(widget=forms.HiddenInput(), initial="Being cute")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove empty choices ("---------") from RadioSelect fields
        for field_name in ['gender', 'energy_level', 'social_style', 'bonding_style', 'activity_cycle']:
            if field_name in self.fields:
                self.fields[field_name].choices = [
                    c for c in self.fields[field_name].choices if c[0] != ''
                ]

    def clean_species(self):
        data = self.cleaned_data['species']
        # Normalize to Title Case to match model choices (e.g. "wolf" -> "Wolf")
        return data.title()

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data.title()


