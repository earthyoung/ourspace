# Generated by Django 4.2.7 on 2023-12-05 06:26

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_post_group'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
