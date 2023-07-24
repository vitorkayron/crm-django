# Generated by Django 4.2.3 on 2023-07-24 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_saldo_faturamento_alter_venda_valor_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='qtd_vendas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='saldo',
            name='faturamento',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='saldo',
            name='produto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_venda',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
