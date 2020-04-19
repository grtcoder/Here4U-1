# Generated by Django 3.0.5 on 2020-04-19 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0010_auto_20200418_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdata',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
