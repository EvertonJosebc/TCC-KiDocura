# Generated by Django 4.2.7 on 2024-01-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='espaco_estoque',
            field=models.IntegerField(default=1),
        ),
    ]