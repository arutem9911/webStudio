from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title
