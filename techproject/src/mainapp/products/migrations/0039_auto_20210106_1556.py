# Generated by Django 3.1.3 on 2021-01-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20210105_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees')], max_length=60),
        ),
    ]