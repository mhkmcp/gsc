from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Member


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'passport',  'date_of_birth', 'city', 'country', 'member_type']
        # exclude = ()


month_choice = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December')
)


class QueryForm(forms.Form):
    month = forms.ChoiceField(label='Select a Month', choices=month_choice, widget=forms.Select)
    year = forms.IntegerField(min_value=2000, max_value=3000)
