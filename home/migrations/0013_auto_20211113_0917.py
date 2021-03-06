# Generated by Django 3.2.8 on 2021-11-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_stock_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Discount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Due_left',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Rate',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Cost',
            field=models.DecimalField(decimal_places=2, max_digits=18),
        ),
    ]
