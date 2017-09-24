from django.contrib import admin
from rango.models import Category,Page
# Register your models her


class PageInline(admin.StackedInline):
    model = Page
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        ('Category information', {'fields': ['views', 'likes']})
    ]
    inlines = [PageInline]





admin.site.register(Category, CategoryAdmin)
# admin.site.register(Page)