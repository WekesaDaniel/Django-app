# Generated by Django 5.0.4 on 2024-04-18 18:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_item_image_alter_userdetail_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
