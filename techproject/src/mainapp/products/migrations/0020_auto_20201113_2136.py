# Generated by Django 3.1.3 on 2020-11-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20201110_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]