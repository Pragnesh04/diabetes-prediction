# Generated by Django 3.2.9 on 2022-03-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usersaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersaddress',
            name='zip_code',
            field=models.IntegerField(max_length=11),
        ),
    ]
