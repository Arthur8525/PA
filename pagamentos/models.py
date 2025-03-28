from django.db import models

class Pagamento(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.CharField(max_length=10)
    data_vencimento = models.DateField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pedentes'), ('pago', 'Pago')])

    def __str__(self):
        return self.descricao