from django.db import models

# Create your models here.
class Schedule(models.Model):
    name = models.CharField('Nome Completo', max_length=50)
    email = models.EmailField('E-mail',null=False, blank=False)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    service = models.CharField('Serviço', max_length=50)
    worker = models.CharField('Profissional', max_length=50)  
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return self.name