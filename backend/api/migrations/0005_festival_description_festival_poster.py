# Generated by Django 5.1.5 on 2025-02-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_festival_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='festival',
            name='poster',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
