# Generated by Django 4.0.4 on 2022-07-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov', '0004_remove_homiyqushish_talabaga_talaba_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homiyarizasi',
            name='Balans',
            field=models.IntegerField(default='0'),
        ),
    ]
