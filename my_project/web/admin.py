from django.contrib import admin
from web.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at', 'author']
    list_filter = ['id', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    fields = ['title', 'description']


admin.site.register(Order, OrderAdmin)
