# Generated by Django 4.2.7 on 2023-12-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('create_ad', models.DateTimeField(auto_now_add=True)),
                ('fruta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='production.fruta')),
                ('produtor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.produtor')),
            ],
        ),
    ]
