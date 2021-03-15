from django.shortcuts import render
from src.models import Member

def unapproved_members(request):
    unapproved_members = Member.objects.filter()
