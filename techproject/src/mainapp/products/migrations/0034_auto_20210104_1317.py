# Generated by Django 3.1.2 on 2021-01-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20210104_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
