# Generated by Django 5.0.2 on 2024-04-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0013_author_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
