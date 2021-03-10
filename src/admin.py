from django.contrib import admin
from .models import Member


# class MemberAdmin(admin.ModelAdmin):
#     # list_display = ['__all__']
#     pass


admin.site.register(Member)
