from django.contrib import admin
from web.models import Order, FileAttachment, ImageAttachment, Status


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at', 'author', 'status']
    list_filter = ['id', 'created_at', 'updated_at', 'author', 'status']
    search_fields = ['title', 'description', 'author', 'status']
    fields = ['title', 'description', 'author']


class ImageAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'image']
    list_filter = ['order']
    search_fields = ['order']
    fields = ['order', 'image']


class FileAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'document']
    list_filter = ['order']
    search_fields = ['order']
    fields = ['order', 'document']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    fields = ['title']


admin.site.register(Order, OrderAdmin)
admin.site.register(FileAttachment, FileAttachmentAdmin)
admin.site.register(ImageAttachment, ImageAttachmentAdmin)
admin.site.register(Status, StatusAdmin)
