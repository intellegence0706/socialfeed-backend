# Generated by Django 5.1.1 on 2024-09-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schema', '0010_schedulevideo_instagram_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialconfig',
            name='twitter_access_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialconfig',
            name='twitter_access_token_secret',
            field=models.TextField(blank=True, null=True),
        ),
    ]
