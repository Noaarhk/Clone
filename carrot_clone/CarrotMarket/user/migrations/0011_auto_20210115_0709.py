# Generated by Django 3.1 on 2021-01-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210114_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pics',
            field=models.ImageField(default='dafault.jpg', upload_to=''),
        ),
    ]
