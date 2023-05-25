from django.contrib import admin
from .models import Category, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
    )
    ordering = ('pk', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
        'parent',
    )

    ordering = ('name', 'parent')

