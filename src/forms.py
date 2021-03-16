from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Member


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class MemberForm(ModelForm):
    class Meta:
        model = Member
        # fields = ['__all__']
        exclude = ['updated_at',]