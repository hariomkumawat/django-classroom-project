# Generated by Django 4.0 on 2022-04-11 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_register_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_model',
            name='dor',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
