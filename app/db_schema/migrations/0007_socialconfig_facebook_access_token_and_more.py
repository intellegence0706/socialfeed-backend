# Generated by Django 5.1.1 on 2024-09-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schema', '0006_schedulevideo_added_by_schedulevideo_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialconfig',
            name='facebook_access_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialconfig',
            name='facebook_app_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialconfig',
            name='facebook_client_secret',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialconfig',
            name='instagram_busiess_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialconfig',
            name='provider',
            field=models.CharField(choices=[('YOUTUBE', 'YOUTUBE'), ('TIKTOK', 'TIKTOK'), ('INSTAGRAM', 'INSTAGRAM')], default='YOUTUBE', max_length=10),
        ),
    ]
