from django.forms import ModelForm, Form
from .models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        # fields = ['__all__']
        exclude = ['updated_at',]