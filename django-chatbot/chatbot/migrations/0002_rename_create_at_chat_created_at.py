# Generated by Django 4.0.6 on 2023-06-27 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
