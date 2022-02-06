# Generated by Django 3.2.8 on 2021-12-05 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20211204_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.news')),
            ],
        ),
    ]