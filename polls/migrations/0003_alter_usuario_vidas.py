# Generated by Django 5.0.2 on 2024-04-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='vidas',
            field=models.DecimalField(decimal_places=0, default=6, max_digits=1),
        ),
    ]