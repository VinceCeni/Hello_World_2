# Generated by Django 3.1.3 on 2020-11-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20201115_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]
