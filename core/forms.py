from django import forms
from django.contrib.auth.models import User
from .models import AnimalProfile


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("No user found with this email.")
        return email


class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        label="New Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
        label="Confirm New Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data



class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Luna'}),
            'gender': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 4'}),
            'energy_level': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'social_style': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'bonding_style': forms.RadioSelect(attrs={'class': 'btn-check'}),
            'preference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Strong companion'}),
        }
    
    species = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wolf'}),
        required=True,
        error_messages={'required': 'Please provide a species.'}
    )
    
    # Explicitly defining image to make it required
    image = forms.ImageField(
        required=True, 
        error_messages={'required': 'Please upload a beautiful photo of your pet! 📸🐾'},
        widget=forms.FileInput(attrs={'class': 'd-none', 'id': 'id_image', 'onchange': 'previewImage(this)'})
    )

    # Choice-based fields for Chips
    activity_cycle = forms.ChoiceField(
        choices=[('Day', 'Day'), ('Night', 'Night'), ('Any', 'Any')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Active During"
    )
    
    favorite_activity = forms.ChoiceField(
        choices=[
            ('Chasing Lasers', 'Chasing Lasers'), ('Playing Fetch', 'Playing Fetch'),
            ('Sunbathing', 'Sunbathing'), ('Bird Watching', 'Bird Watching'),
            ('Belly Rubs', 'Belly Rubs'), ('Other', 'Other')
        ],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Favorite Activity"
    )

    habitat = forms.ChoiceField(
        choices=[('Forest', 'Forest'), ('Jungle', 'Jungle'), ('Desert', 'Desert'), ('Ocean', 'Ocean'), ('Urban', 'Urban'), ('Other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Favorite Habitat"
    )

    territory = forms.ChoiceField(
        choices=[('Mountains', 'Mountains'), ('River', 'River'), ('Garden', 'Garden'), ('House', 'House'), ('Cave', 'Cave'), ('Other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Home Territory"
    )

    personality = forms.ChoiceField(
        choices=[('Playful', 'Playful'), ('Loyal', 'Loyal'), ('Protective', 'Protective'), ('Calm', 'Calm'), ('Mischievous', 'Mischievous'), ('Other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Personality"
    )

    diet = forms.ChoiceField(
        choices=[('Carnivore', 'Carnivore'), ('Herbivore', 'Herbivore'), ('Omnivore', 'Omnivore'), ('Insectivore', 'Insectivore'), ('Other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Diet Style"
    )

    preference = forms.ChoiceField(
        choices=[('Strong Companion', 'Strong Companion'), ('Playful Friend', 'Playful Friend'), ('Gentle Soul', 'Gentle Soul'), ('Adventurer', 'Adventurer'), ('Cuddle Buddy', 'Cuddle Buddy'), ('Other', 'Other')],
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        required=True,
        label="Match Preference"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Standardize required messages (preserving custom image message)
        for field_name, field in self.fields.items():
            if field.required and field_name != 'image':
                label = field.label.lower() if field.label else field_name.replace('_', ' ')
                field.error_messages['required'] = f"Please provide a {label}."

        chip_fields = [
            'gender', 'energy_level', 'social_style', 'bonding_style', 
            'activity_cycle', 'favorite_activity', 'habitat', 
            'territory', 'personality', 'diet', 'preference'
        ]
        for field_name in chip_fields:
            if field_name in self.fields:
                self.fields[field_name].choices = [
                    c for c in self.fields[field_name].choices if c[0] != ''
                ]

    def clean_species(self):
        data = self.cleaned_data['species'].strip().title()
        valid_species = [choice[0] for choice in AnimalProfile.SPECIES_CHOICES]
        
        if data not in valid_species:
            raise forms.ValidationError(f"'{data}' is not a supported species yet. Try one of our partners! 🐾")
        return data

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data.title()


