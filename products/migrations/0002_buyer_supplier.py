# Generated by Django 4.0.3 on 2022-04-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=255)),
                ('buyer_contact_no', models.CharField(max_length=100)),
                ('buyer_email', models.CharField(max_length=100)),
                ('buyer_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_contact_no', models.CharField(max_length=100)),
                ('supplier_email', models.CharField(max_length=100)),
                ('supplier_address', models.CharField(max_length=255)),
            ],
        ),
    ]
