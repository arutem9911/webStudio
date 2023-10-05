from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'photo', 'birth_date')
    list_filter = ['birth_date']


admin.site.register(User, CustomUserAdmin)
