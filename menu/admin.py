from django.contrib import admin
from menu.models import Menu, Category, Item


class ItemInline(admin.TabularInline):
    model = Item


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


class CategoryInline(admin.TabularInline):
    model = Category


class MenuAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
