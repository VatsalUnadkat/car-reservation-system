# Generated by Django 3.2.15 on 2022-09-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('vehicle_model', models.CharField(max_length=255)),
                ('licence_number', models.CharField(max_length=50, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
