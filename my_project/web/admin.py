from django.contrib import admin
from web.models import Order, FileAttachment, ImageAttachment


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at', 'author']
    list_filter = ['id', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    fields = ['title', 'description']


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


admin.site.register(Order, OrderAdmin)
admin.site.register(FileAttachment, FileAttachmentAdmin)
admin.site.register(ImageAttachment, ImageAttachmentAdmin)
