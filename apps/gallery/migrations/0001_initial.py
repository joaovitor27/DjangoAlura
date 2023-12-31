# Generated by Django 4.2.3 on 2023-07-17 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Legenda')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('image', models.CharField(max_length=150, verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Fotografia',
                'verbose_name_plural': 'Fotografias',
            },
        ),
    ]
