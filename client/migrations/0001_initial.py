# Generated by Django 3.0.5 on 2020-05-01 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=1000)),
                ('extra_data', models.FileField(blank=True, null=True, upload_to='client/uploads')),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Counsellordata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')])),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Profile_pic', models.FileField(blank=True, null=True, upload_to='')),
                ('Email', models.EmailField(max_length=254)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('Education', models.CharField(blank=True, max_length=300, null=True)),
                ('Expertise', models.CharField(blank=True, max_length=200, null=True)),
                ('Summary', models.CharField(blank=True, max_length=1000, null=True)),
                ('Consultation_start', models.TimeField(null=True)),
                ('Consultation_end', models.TimeField(null=True)),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clientdata',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('0', 'Male'), ('1', 'Female'), ('2', 'Others')], max_length=32)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('State', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('Marital_Status', models.CharField(choices=[('0', 'Single'), ('1', 'Commited'), ('2', 'Divorced'), ('3', 'Married')], max_length=32)),
                ('Educational_Status', models.CharField(choices=[('0', '10th Pass'), ('1', '12th Pass'), ('2', 'Graduate'), ('3', 'Post_Graduate'), ('4', 'Doctorate'), ('5', 'Post_Doc')], max_length=32)),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ids', models.IntegerField(blank=True, null=True)),
                ('counsellor_ids', models.IntegerField(blank=True, null=True)),
                ('Booking_time', models.TimeField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_user', to=settings.AUTH_USER_MODEL)),
                ('counsellor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='counsellor_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveCounsellor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_time', models.TimeField(null=True)),
                ('Counsellor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='counsellor_id_clside', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_id_clside', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_time', models.TimeField(null=True)),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_id_coun', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='counsellor_id_coun', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
