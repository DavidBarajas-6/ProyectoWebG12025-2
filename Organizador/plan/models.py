from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tipo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.name

class Plan(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    realizado = models.BooleanField(default=False)
    comidas=models.ManyToManyField('Comida',through='Menu')
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Planes"
    def __str__(self):
        return self.title
    @property
    def calorias_totales(self):
        total = 0
        for menu in self.menu_set.all():
            total += menu.comida.calorias * menu.cantidad
        return total

class Comida(models.Model):
    name = models.CharField(max_length=50)
    calorias = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    cantidad=models.IntegerField()


    
