# Generated by Django 3.2.8 on 2021-11-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_saving_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='Amount',
            field=models.IntegerField(),
        ),
    ]
