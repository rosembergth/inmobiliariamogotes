# Generated by Django 3.2.5 on 2021-08-25 01:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaprod',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
