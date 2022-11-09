from django.contrib.auth.models import User
from account.models import Profile
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# nota: django has a UserCreationForm from django.contrib.auth.forms
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
