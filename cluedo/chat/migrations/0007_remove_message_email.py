# Generated by Django 4.0.6 on 2022-07-08 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
    ]
