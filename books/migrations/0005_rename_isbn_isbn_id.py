# Generated by Django 3.2 on 2021-04-22 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210422_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='isbn',
            old_name='isbn',
            new_name='id',
        ),
    ]
