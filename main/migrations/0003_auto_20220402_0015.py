# Generated by Django 3.2.9 on 2022-04-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220313_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='model1_prediction',
            field=models.CharField(default='0%', max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='model2_prediction',
            field=models.CharField(default='0%', max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='model3_prediction',
            field=models.CharField(default='0%', max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='model4_prediction',
            field=models.CharField(default='0%', max_length=10),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='result',
            field=models.CharField(default='0%', max_length=10),
        ),
    ]
