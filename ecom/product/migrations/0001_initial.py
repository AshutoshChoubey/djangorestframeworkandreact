# Generated by Django 3.0.2 on 2020-01-30 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('descripition', models.CharField(max_length=255, null=True)),
                ('image', models.CharField(max_length=255, null=True)),
                ('price', models.IntegerField(null=True)),
                ('compare_price', models.IntegerField(null=True)),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 2, 29, 11, 57, 19, 845033))),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]