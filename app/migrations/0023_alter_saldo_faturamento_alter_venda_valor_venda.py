# Generated by Django 4.2.3 on 2023-07-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_saldo_produto_alter_venda_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='faturamento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_venda',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
