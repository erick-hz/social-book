# Generated by Django 4.0.5 on 2022-06-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followerscount_likepost_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
