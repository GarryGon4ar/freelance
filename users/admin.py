from django.contrib import admin
from users.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'user_type', 'balance')


admin.site.register(CustomUser, UserAdmin)
