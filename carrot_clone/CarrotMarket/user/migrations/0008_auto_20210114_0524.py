# Generated by Django 3.1 on 2021-01-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210113_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pics',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
