from django.contrib import admin

from .models import (Ingredient, Tag, Recipe, IngredientTemp, ShoppingCart,
                     Favorite, Subscription)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
    search_fields = ('author', 'name', 'tags',)
    list_filter = ('tags',)
    empty_value_display = '-пусто-'


class IngredientTempAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ingredient', 'recipe', 'amount')
    list_filter = ('ingredient',)
    empty_value_display = '-пусто-'


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'image', 'cooking_time')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'image', 'cooking_time')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientTemp, IngredientTempAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
