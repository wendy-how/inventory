# Generated by Django 5.0.1 on 2024-02-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outbound', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outbound',
            name='date_shipped',
            field=models.IntegerField(),
        ),
    ]
