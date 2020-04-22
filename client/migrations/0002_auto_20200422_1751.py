# Generated by Django 3.0.5 on 2020-04-22 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeclient',
            name='Client',
        ),
        migrations.AddField(
            model_name='activeclient',
            name='Client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_id_coun', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='activecounsellor',
            name='Counsellor',
        ),
        migrations.AddField(
            model_name='activecounsellor',
            name='Counsellor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='counsellor_id_clside', to=settings.AUTH_USER_MODEL),
        ),
    ]