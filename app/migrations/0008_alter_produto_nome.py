# Generated by Django 4.1.5 on 2023-07-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_saldo_saldo_faturamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
