# Generated by Django 2.2.10 on 2021-07-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterinfo',
            name='end_time',
            field=models.DateTimeField(verbose_name='喝完一杯水'),
        ),
    ]
