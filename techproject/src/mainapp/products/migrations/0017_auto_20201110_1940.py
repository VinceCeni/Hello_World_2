# Generated by Django 3.1.3 on 2020-11-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20201110_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
