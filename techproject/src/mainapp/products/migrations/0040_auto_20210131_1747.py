# Generated by Django 3.1.3 on 2021-01-31 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20210106_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
