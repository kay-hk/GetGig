# Generated by Django 5.1.5 on 2025-02-14 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_ticket_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='uemail',
            field=models.ForeignKey(db_column='uemail', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
