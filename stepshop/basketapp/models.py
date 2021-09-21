from django.db import models

from mainapp.models import Product
from stepshop import settings

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    def __str__(self):
        return self.name or f'Id корзины - {self.pk}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
