# Generated by Django 5.1.6 on 2025-02-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='ean',
            field=models.IntegerField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
