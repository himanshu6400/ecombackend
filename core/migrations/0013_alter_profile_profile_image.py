# Generated by Django 4.0.6 on 2022-08-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, max_length=255, upload_to='user_profile_image'),
        ),
    ]