# Generated by Django 3.1.3 on 2020-11-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20201113_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('treats', 'treats')], max_length=60),
        ),
    ]
