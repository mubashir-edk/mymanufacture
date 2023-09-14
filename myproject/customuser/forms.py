
from typing import Any, Dict
from django import forms
from customuser.models import CustomUser
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    # confirm_password = forms.CharField()
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter Password',
        'id': 'formConfirmPassword',
    }))
    class Meta:
        model = CustomUser
        exclude = ('is_active','last_login','user_permissions','groups')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username',
                'id': 'formUsername',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a valid Email',
                'id': 'formEmail',
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Designation',
                'id': 'formDesignation',
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Mobile',
                'id': 'formMobile',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password',
                'id': 'formPassword',
            }),
            # 'confirm_password': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Re-enter Password',
            #     'id': 'formConfirmpassword',
            # }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'formIsstaff',
            }),
            'is_superuser': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'formIssuperuser',
            }),
        }
    
    def clean(self) -> Dict[str, Any]:
        super().clean()
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError({"confirm_password":"Password must be same"})
        return 
    
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Username', 
                'id': 'formUsername', 
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Password', 
                'id': 'formPassword', 
            }),
        }