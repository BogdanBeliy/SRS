from django.contrib import admin
from account.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'status', 'payment_status')
    search_fields = ('status', 'payment_status')
    list_filter = ('status', 'payment_status')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields = (' name', 'unp', 'address')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('name', 'org', 'favorite_type')
    search_fields = ('name', 'org', 'favorite_type')
