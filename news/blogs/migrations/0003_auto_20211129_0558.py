# Generated by Django 3.2.8 on 2021-11-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_news_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'New'},
        ),
        migrations.AddField(
            model_name='news',
            name='pk_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
