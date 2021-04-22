# Generated by Django 3.2 on 2021-04-22 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_auto_20210422_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='isbn',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boooks', to=settings.AUTH_USER_MODEL),
        ),
    ]
