# Generated by Django 3.1.3 on 2020-11-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201109_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]
