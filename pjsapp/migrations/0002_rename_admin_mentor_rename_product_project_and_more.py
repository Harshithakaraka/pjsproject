# Generated by Django 4.1.7 on 2023-03-31 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pjsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Mentor',
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='Team',
        ),
    ]
