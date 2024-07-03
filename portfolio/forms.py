from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")
        return cleaned_data

class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    )
    email = forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''})
    )
    text = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''})
    )
