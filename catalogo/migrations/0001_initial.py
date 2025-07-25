# Generated by Django 5.2.4 on 2025-07-13 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "nome",
                    models.CharField(max_length=255, verbose_name="Nome do Produto"),
                ),
                (
                    "descricao",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descrição do Produto"
                    ),
                ),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Preço Unitário"
                    ),
                ),
                (
                    "quantidade_estoque",
                    models.IntegerField(verbose_name="Quantidade em Estoque"),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="produtos_gerenciados",
                        to="contas.administrador",
                        verbose_name="Administrador Responsável",
                    ),
                ),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Servico",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "nome",
                    models.CharField(max_length=255, verbose_name="Nome do Serviço"),
                ),
                (
                    "descricao",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descrição do Serviço"
                    ),
                ),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Preço do Serviço"
                    ),
                ),
                (
                    "duracao_estimada",
                    models.DurationField(verbose_name="Duração Estimada"),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="servicos_gerenciados",
                        to="contas.administrador",
                        verbose_name="Administrador Responsável",
                    ),
                ),
            ],
            options={
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
                "ordering": ["nome"],
            },
        ),
    ]
