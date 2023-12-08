# Generated by Django 4.1 on 2023-12-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=20, verbose_name='cpf')),
                ('cell_phone', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'Profissional',
                'verbose_name_plural': 'Profissionais',
                'ordering': ['id'],
            },
        ),
    ]