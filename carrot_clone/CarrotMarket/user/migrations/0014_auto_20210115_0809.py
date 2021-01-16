# Generated by Django 3.1 on 2021-01-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20210115_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, db_index=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, db_index=True, max_length=13, unique=True),
        ),
    ]
