# Generated by Django 3.2.9 on 2022-04-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220402_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='diabetes_pedigree_function',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]
