# Generated by Django 5.0.6 on 2024-06-25 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='chaivariety',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 15, 40, 40, 619536, tzinfo=datetime.timezone.utc)),
        ),
    ]
