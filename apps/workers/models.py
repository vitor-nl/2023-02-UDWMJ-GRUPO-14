from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('cpf', max_length=20)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering =['id']

    def __str__(self):
        return self.name