from django.contrib import admin
from .models import FoodUser


class FoodUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff',)
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'


admin.site.register(FoodUser, FoodUserAdmin)