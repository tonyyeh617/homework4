# Generated by Django 4.2.11 on 2024-04-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature_db',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
