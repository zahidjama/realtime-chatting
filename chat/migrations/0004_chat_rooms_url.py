# Generated by Django 4.1.7 on 2023-04-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chattings_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_rooms',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
