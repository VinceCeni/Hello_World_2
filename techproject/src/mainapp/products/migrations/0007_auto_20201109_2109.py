# Generated by Django 3.1.3 on 2020-11-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201109_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
