# Generated by Django 5.1.3 on 2024-11-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='iata_code',
            field=models.CharField(db_index=True, max_length=3, unique=True),
        ),
    ]
