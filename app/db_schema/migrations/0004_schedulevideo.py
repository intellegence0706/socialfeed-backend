# Generated by Django 5.1.1 on 2024-09-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_schema', '0003_socialconfig_added_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='schedule_videos/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
