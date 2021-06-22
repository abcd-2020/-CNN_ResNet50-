from django.contrib import admin
from .models import Prod_m

class ProductAdmin(admin.ModelAdmin):#admin에서 name으로 검색기능
    search_fields = ['name']
admin.site.register(Prod_m, ProductAdmin)