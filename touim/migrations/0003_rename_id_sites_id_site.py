# Generated by Django 3.2.2 on 2021-05-10 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touim', '0002_auto_20210510_0532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites',
            old_name='id',
            new_name='id_site',
        ),
    ]