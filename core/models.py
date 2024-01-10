from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_eventO(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        return self.data_evento < timezone.localtime(timezone.now())

    def get_evento_que_falta_menos_de_1h(self):
        now = timezone.now()
        return now > self.data_evento - timedelta(hours=1) and now < self.data_evento