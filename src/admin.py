from django.contrib import admin
from .models import Member, Subscription


class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'passport', 'member_type', 'phone', 'city', 'country']
    list_filter = ['member_type', 'country']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['member', 'amount', 'month', 'year', 'payment_date']
    list_filter = ['month', 'year']


admin.site.register(Member, MemberAdmin)
admin.site.register(Subscription, SubscriptionAdmin)

