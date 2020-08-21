from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insert password'
            }
        )
    )

    password2 = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat password'
            }
            )
    )
    class Meta:
        model=CustomUser
        fields=('username', 'email')

    def clean_password2(self):
        if self.cleaned_data.get("password1") != self.cleaned_data.get("password2"):
            self.add_error("password2","Passwords don't match")

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
    )

    password = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput(
            )
    )
          
    def clean(self):
        data = super(LoginForm, self).clean()
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']   
        if not authenticate(email=email,password=password):
            raise forms.ValidationError("Invalid Data")
        
        return self.data

class UpdatePasswordForms(forms.Form):
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insert password'
            }
        )
    )

    password2 = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Insert new password'
            }
            )
    )
    
 
    