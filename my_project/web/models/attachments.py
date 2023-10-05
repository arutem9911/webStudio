from django.db import models
import random
import string


class ImageAttachment(models.Model):
    order = models.ForeignKey('web.Order', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', blank=False, null=False)


class FileAttachment(models.Model):
    order = models.ForeignKey('web.Order', on_delete=models.CASCADE, related_name='files')
    document = models.FileField(upload_to='files', blank=False, null=False)


