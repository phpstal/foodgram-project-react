from django.contrib import admin

from .models import (Ingredient, Tag, Recipe, IngredientTemp, ShoppingCart,
                     Favorites, Subscription)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
    search_fields = ('author', 'name', 'tags',)
    list_filter = ('author', 'name', 'tags',)
    empty_value_display = '-пусто-'


class IngredientTempAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ingredient', 'recipe', 'amount')
    list_filter = ('ingredient',)
    empty_value_display = '-пусто-'


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientTemp, IngredientTempAdmin)
admin.site.register(ShoppingCart)
admin.site.register(Favorites)
admin.site.register(Subscription)
