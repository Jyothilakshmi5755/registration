from django.contrib.auth.forms import UserCreationForm
from app7.models import CustomUser
from django import forms
from app7.models import employee


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields= UserCreationForm.Meta.fields+('email','phone')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'