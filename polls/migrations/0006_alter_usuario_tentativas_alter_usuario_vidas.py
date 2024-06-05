# Generated by Django 4.2.11 on 2024-04-22 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_palavradia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tentativas',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='vidas',
            field=models.DecimalField(decimal_places=0, default=6, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
