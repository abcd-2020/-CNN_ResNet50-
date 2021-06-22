import reserve as reserve
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Prod_m(models.Model):
    product_photo = models.ImageField(blank=True, null=True)  # 게시글 Post에 이미지 추가
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    category = models.TextField(verbose_name='상품카테고리')
    product_url = models.TextField(verbose_name='상품링크')
    # product_number = models.IntegerField(default=1)



    def __str__(self):
        return self.name #object 대신 name나오기


os.environ.setdefault("DJANGO_SETTING_ODULE","weather.settings")
django.setup()

from mysite.models import 


