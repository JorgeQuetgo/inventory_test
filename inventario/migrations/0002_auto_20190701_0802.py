# Generated by Django 2.2.2 on 2019-07-01 08:02

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadfile',
            name='jfile',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
