# Generated by Django 4.2.7 on 2024-01-19 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_estoquefruta'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='estoque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='production.estoquefruta'),
        ),
        migrations.AddField(
            model_name='estoquefruta',
            name='quantidade_max',
            field=models.IntegerField(default=50),
        ),
    ]
