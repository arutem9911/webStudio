from django.db import models
import random
import string


def generate_random_id():
    while True:
        new_id = ''.join(random.choice(string.digits) for x in range(6))
        if not Order.objects.filter(pk=new_id).exists():
            return new_id


class Order(models.Model):
    id = models.CharField(max_length=6, primary_key=True, unique=True, editable=False, blank=False, null=False)
    author = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, related_name='summary', null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.id = generate_random_id()
        super().save(*args, **kwargs)
    #
    # class Meta:
    #     abstract = True

