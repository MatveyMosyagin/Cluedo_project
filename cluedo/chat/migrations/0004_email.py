# Generated by Django 4.0.6 on 2022-07-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=10000)),
            ],
        ),
    ]
