# Generated by Django 3.2.8 on 2021-11-25 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
