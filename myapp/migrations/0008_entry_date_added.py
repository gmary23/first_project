# Generated by Django 5.0 on 2023-12-20 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
