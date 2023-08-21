# Generated by Django 2.2.7 on 2020-06-16 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portola', '0010_auto_20200610_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='product_type',
            field=models.CharField(choices=[['modules', 'Modules'], ['racking', 'Racking'], ['inverter', 'Inverter'], ['optimizer', 'Optimizer'], ['Power Electronics', 'Power Electronics']], db_index=True, default='MODULES', max_length=32),
        ),
    ]