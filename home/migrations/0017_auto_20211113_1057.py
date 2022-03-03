# Generated by Django 3.2.8 on 2021-11-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_expenses_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='Discount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='credit',
            name='Due_left',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='credit',
            name='Paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='credit',
            name='Quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='credit',
            name='Rate',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='credit',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
