# Generated by Django 3.2.8 on 2021-11-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_stock_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Cost',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
