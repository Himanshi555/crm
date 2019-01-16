from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from proj1.models import Categary, subcategary, Brand, catalog

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  forms.ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class changeform(UserChangeForm):
    class Meta():
        model = User
        fields = ('username',
                    'email'
                 )

class catgarysform(forms.ModelForm):
    class Meta:
        model = Categary
        fields = '__all__'

class subcatgarysform(forms.ModelForm):
    class Meta:
        model = subcategary
        fields = '__all__'

class brandform(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class catalogform(forms.ModelForm):
    class Meta:
        model = catalog
        fields = '__all__'
