# Generated by Django 4.2.7 on 2024-01-08 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_emaillog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.DeleteModel(
            name='Channel',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
