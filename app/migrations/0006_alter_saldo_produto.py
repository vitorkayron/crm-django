# Generated by Django 4.1.5 on 2023-07-17 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_saldo_data_venda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto'),
        ),
    ]
