# Generated by Django 3.2.8 on 2021-12-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_rename_table_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Crud',
        ),
    ]