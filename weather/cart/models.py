import os

import django
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from mysite.models import Prod_m


class CartList(models.Model):
    #cart_id = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Prod_m, on_delete=models.CASCADE)


    class meta:
        db_table = 'CartList'

    def __str__(self):
        return self.product+'/'+self.user





# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Prod_m, on_delete=models.CASCADE)
#     active = models.BooleanField(default=False)
#     # 수량은 -1 과 같은 수량이 없기 때문에 아래의 필드로 선언하여 최소값을 1 로 설정
#     quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = '장바구니'
#         verbose_name_plural = f'{verbose_name} 목록'
#         ordering = ['-pk']
#
#         def __str__(self):
#             return self.product.name