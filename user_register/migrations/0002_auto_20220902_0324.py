# Generated by Django 3.2.15 on 2022-09-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
