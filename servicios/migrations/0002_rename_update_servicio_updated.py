# Generated by Django 3.2.5 on 2021-08-13 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='update',
            new_name='updated',
        ),
    ]
