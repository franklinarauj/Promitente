from django.db import models

# Create your models here.
class TB_Cliente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, name='cpf', unique=True)
    nome = models.CharField(max_length=60, name='nome')
    email = models.CharField(max_length=40, name='email')
    telefone = models.CharField(max_length=14, name='telefone')

    class Meta:
        db_table = "TB_Cliente"

    def __str__(self):
        return f"{self.nome}"
