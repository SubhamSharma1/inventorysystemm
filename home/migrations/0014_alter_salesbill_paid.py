# Generated by Django 3.2.8 on 2021-11-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211113_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbill',
            name='Paid',
            field=models.IntegerField(),
        ),
    ]
