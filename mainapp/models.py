from django.db import models
from django.contrib.auth.models import User

class Cash(models.Model):
    item = models.CharField(max_length=100,verbose_name="Товар")
    price = models.FloatField(verbose_name="Цена")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Дата")
    type = models.CharField(max_length=100,verbose_name="Тип(касса/закупка)")
    beznal = models.BooleanField(verbose_name="Безналичный рассчет",default=False)

    def __str__(self):
        return self.item