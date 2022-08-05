# Generated by Django 4.0.5 on 2022-07-27 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_delete_userprofilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
