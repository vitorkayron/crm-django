# Generated by Django 4.1.5 on 2023-07-17 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_saldo_saldo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saldo',
            name='data_venda',
        ),
        migrations.RemoveField(
            model_name='saldo',
            name='quantidade_vendida',
        ),
        migrations.AlterField(
            model_name='saldo',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.produto'),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_vendida', models.PositiveIntegerField(default=0)),
                ('data_venda', models.DateField(auto_now_add=True)),
                ('saldo', models.DecimalField(decimal_places=3, default=0, max_digits=1000)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
        ),
    ]
