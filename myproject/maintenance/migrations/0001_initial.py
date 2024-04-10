# Generated by Django 5.0.2 on 2024-02-20 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordertid', models.CharField(max_length=100)),
                ('ordername', models.CharField(max_length=100)),
                ('detial', models.CharField(max_length=120)),
                ('stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('sentrepairby', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
