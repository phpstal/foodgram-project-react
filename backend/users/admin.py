from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff')
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)