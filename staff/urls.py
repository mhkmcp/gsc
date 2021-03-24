from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import index, approve

urlpatterns = [
    path('', index, name='staff-index'),
    path('approve/<int:member_id>', approve, name='approve'),
]
