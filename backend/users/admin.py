from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)