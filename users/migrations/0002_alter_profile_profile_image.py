# Generated by Django 3.2.6 on 2021-08-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.svg', upload_to='profile'),
        ),
    ]