# Generated by Django 3.1.3 on 2020-11-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201105_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
