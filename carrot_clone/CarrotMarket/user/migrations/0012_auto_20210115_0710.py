# Generated by Django 3.1 on 2021-01-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210115_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pics',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]