# Generated by Django 3.2.8 on 2021-11-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_salesbill_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saving',
            name='Amount',
            field=models.IntegerField(),
        ),
    ]