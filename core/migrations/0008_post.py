# Generated by Django 4.0.5 on 2022-07-04 16:25

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_like', models.IntegerField(default=0)),
            ],
        ),
    ]
