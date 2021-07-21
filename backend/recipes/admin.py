from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientTemp, Recipe,
                     ShoppingCart, Subscription, Tag)


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
    search_fields = ('author', 'name', 'tags', 'ingredients')
    list_filter = ('author', 'name', 'tags', 'ingredients')
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
admin.site.register(Favorite)
admin.site.register(Subscription)
