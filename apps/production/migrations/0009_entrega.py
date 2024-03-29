# Generated by Django 4.2.7 on 2024-01-31 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
        ('production', '0008_estoquepolpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_entregue', models.FloatField()),
                ('data_producao', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.cliente')),
                ('estoque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='production.estoquepolpa')),
            ],
        ),
    ]
