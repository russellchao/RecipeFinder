from django.contrib import admin

from .models import Category, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category_text"]}),
    ]

    inlines = [ChoiceInline]
    

admin.site.register(Category, CategoryAdmin)