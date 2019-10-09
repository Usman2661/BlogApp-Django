# Generated by Django 2.2.6 on 2019-10-09 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostTitle', models.CharField(max_length=200)),
                ('PostMessage', models.TextField(blank=True)),
                ('Image', models.ImageField(upload_to='photos')),
                ('UserID', models.ImageField(upload_to='')),
                ('Catagory', models.CharField(max_length=200)),
                ('DateTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]