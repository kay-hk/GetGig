# Generated by Django 5.1.5 on 2025-02-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_ticket_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickettype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='tickettype',
            table='tickettype',
        ),
    ]
