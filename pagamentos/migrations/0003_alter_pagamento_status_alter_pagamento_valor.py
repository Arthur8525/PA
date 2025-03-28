# Generated by Django 5.1.7 on 2025-03-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamentos', '0002_alter_pagamento_status_alter_pagamento_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pedentes'), ('pago', 'Pago')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='valor',
            field=models.CharField(max_length=10),
        ),
    ]
