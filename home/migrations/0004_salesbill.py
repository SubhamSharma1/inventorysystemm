# Generated by Django 3.2.8 on 2021-11-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salesbill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Customer_name', models.CharField(max_length=255)),
                ('Customer_phone', models.CharField(max_length=255)),
                ('Customer_address', models.CharField(max_length=255)),
                ('Paid', models.CharField(max_length=255)),
            ],
        ),
    ]
