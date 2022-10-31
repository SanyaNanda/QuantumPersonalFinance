# Generated by Django 4.0.5 on 2022-10-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_alter_expensecategory_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='note',
            field=models.FloatField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='note',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
