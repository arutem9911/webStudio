# Generated by Django 3.2.20 on 2023-10-07 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
