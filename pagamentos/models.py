from django.db import models

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
    ]

    descricao = models.CharField("Descrição", max_length=255)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data_vencimento = models.DateField("Data de Vencimento")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor} ({self.get_status_display()})"
