# Generated by Django 3.0.8 on 2020-09-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='mnpComment',
        ),
    ]
