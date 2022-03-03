# Generated by Django 3.2.8 on 2021-11-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_purchasebill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasebillitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Company_name', models.CharField(max_length=255)),
                ('Customer_phone', models.CharField(max_length=255)),
                ('Customer_address', models.CharField(max_length=255)),
                ('Product', models.CharField(max_length=255)),
                ('Quantity', models.CharField(max_length=255)),
                ('Rate', models.CharField(max_length=255)),
                ('Discount', models.CharField(max_length=255)),
                ('Total', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-Date',),
            },
        ),
    ]
