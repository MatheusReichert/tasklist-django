from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.db import models

# Create your models here.
# class Pessoa(models.Model):
#     nome = models.CharField(max_length=255, default="nulo")

#     def __str__(self):
#         return self.nome
    

#     class Meta:
#         verbose_name = ("Pessoa")
#         verbose_name_plural = ("Pessoas")

class Priority(ChoiceEnum):
    HIGH = "Alta"
    MEDIUM = "Média"
    LOW = "Baixa"

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="nome", max_length=100)
    description = models.CharField(verbose_name="descrição", max_length=1000)
    priority = EnumChoiceField(enum_class=Priority, default=Priority.LOW)
     
