# Generated by Django 5.1 on 2024-08-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_room_message_chat_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_profile_complete',
            field=models.BooleanField(default=False),
        ),
    ]
