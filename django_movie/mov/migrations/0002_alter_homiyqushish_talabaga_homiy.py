# Generated by Django 4.0.4 on 2022-07-19 15:16

from django.db import migrations, models
import mov.models


class Migration(migrations.Migration):

    dependencies = [
        ('mov', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homiyqushish_talabaga',
            name='homiy',
            field=models.CharField(max_length=120, verbose_name=mov.models.HomiyArizasi),
        ),
    ]
