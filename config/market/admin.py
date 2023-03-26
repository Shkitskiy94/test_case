from django.contrib import admin

from .models import (Product, Warehouse, WarehouseProduct,
                     Client, ClientProduct, Order)

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(WarehouseProduct)
admin.site.register(Client)
admin.site.register(ClientProduct)
admin.site.register(Order)
