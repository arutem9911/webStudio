from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['first_name', 'last_name', 'city']


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline]
    ordering = ('username', 'email', 'phone', 'photo', 'birth_date')


admin.site.register(User, UserProfileAdmin)
