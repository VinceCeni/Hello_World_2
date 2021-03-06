# Generated by Django 3.1.2 on 2021-01-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20201120_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60)),
                ('name', models.CharField(blank=True, default='', max_length=60)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
                ('image', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
