# Generated by Django 5.0.2 on 2024-04-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_rename_work_order_work_request_work_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_request',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
