# Generated by Django 3.0.8 on 2020-09-14 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phoneno', models.CharField(help_text='omit country codes like +234', max_length=15, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Professional')], max_length=1)),
                ('confirmed_email', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(default='profiles/profile.png', upload_to='profiles')),
                ('id_photo', models.ImageField(default='user_ids/id.png', upload_to='user_ids')),
                ('ip', models.GenericIPAddressField(blank=True, editable=False, null=True)),
                ('address', models.TextField()),
                ('geolocation', models.CharField(blank=True, editable=False, max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('userx', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
