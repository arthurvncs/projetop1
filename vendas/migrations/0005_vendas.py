# Generated by Django 3.2 on 2021-04-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_rename_fornecedor_fornecedore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ome', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
