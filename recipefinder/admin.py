from django.contrib import admin

from .models import Category, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fields = ('choice_text', 'selected')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category_text"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id', 'category_text')
    search_fields = ('category_text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'category', 'selected')
    list_filter = ('category', 'selected')
    search_fields = ('choice_text',)
    list_editable = ('selected',)


# admin.site.register(Category, CategoryAdmin)