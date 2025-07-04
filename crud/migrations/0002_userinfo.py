# Generated by Django 4.2.23 on 2025-06-26 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panCard', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('profile_pic', models.ImageField(upload_to='', verbose_name='profile_pic/')),
                ('panCard_Image', models.ImageField(upload_to='', verbose_name='pancard/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
