# Generated by Django 3.1.3 on 2020-11-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201105_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]