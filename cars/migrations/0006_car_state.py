# Generated by Django 5.0.2 on 2024-03-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='state',
            field=models.TextField(null=True),
        ),
    ]
