# Generated by Django 3.2.22 on 2023-11-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlab_app', '0004_auto_20231106_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_table',
            name='qualification',
            field=models.CharField(max_length=500),
        ),
    ]
