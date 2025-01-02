# streakpy/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Customizing the UserCreationForm if needed
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


from .models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter habit name'}),
        }
