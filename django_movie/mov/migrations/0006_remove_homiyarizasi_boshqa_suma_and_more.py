# Generated by Django 4.0.4 on 2022-07-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov', '0005_homiyarizasi_balans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homiyarizasi',
            name='boshqa_suma',
        ),
        migrations.RemoveField(
            model_name='homiyarizasi',
            name='tulov_suma',
        ),
        migrations.AlterField(
            model_name='homiyarizasi',
            name='Balans',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
