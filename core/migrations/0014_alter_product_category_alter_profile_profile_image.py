# Generated by Django 4.0.6 on 2022-08-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Cosmetic', 'Cosmetic'), ('Toys', 'Toys'), ('Jeans', 'Jeans')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='user_profile_image'),
        ),
    ]
