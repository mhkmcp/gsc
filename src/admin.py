from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'passport', 'member_type', 'is_active']
    list_filter = ['is_active']


# admin.site.register(Member)
