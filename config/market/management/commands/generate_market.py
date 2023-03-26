import random
from django.core.management.base import BaseCommand
from market.models import (Product, Warehouse, WarehouseProduct,
                           Client, ClientProduct, Order)
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate market offers'

    def handle(self, *args, **options):
        """Импорт базовых настроек"""
        products_list = settings.PRODUCT_LIST
        warehouses_count = settings.WAREHOUSES_COUNT
        clients_count = settings.CLIENTS_COUNT
        iterations_count = settings.ITERATIONS_COUNT

        """Генерация продуктов"""
        products = []
        for product_name in products_list:
            product, created = Product.objects.get_or_create(name=product_name)
            products.append(product)
        """Генерация складов"""
        warehouses = []
        for i in range(warehouses_count):
            warehouse = Warehouse.objects.create(
                name=f'Warehouse_{i}',
                limit=random.randint(50, 200),
                tariff=random.uniform(1, 10)
            )
            """Добавление случайных товаров на склады с ограничениями"""
            for product in random.sample(products,
                                         k=random.randint(1, len(products))):
                limit = random.randint(10, int(warehouse.limit/2))
                WarehouseProduct.objects.create(
                    warehouse=warehouse,
                    product=product,
                    limit=limit
                )
            warehouses.append(warehouse)
        """Генерация клиентов"""
        clients = []
        for i in range(clients_count):
            client = Client.objects.create(name=f'Client_{i}')

            """Добавление случайных продуктов клиенту"""
            for product in random.sample(products,
                                         k=random.randint(1, len(products))):
                quantity = random.randint(1, 50)
                ClientProduct.objects.create(
                    client=client,
                    product=product,
                    quantity=quantity
                )
            clients.append(client)
        """Генерация заказов для каждой итерации"""
        for i in range(iterations_count):
            print(f'Итерация {i+1}/{iterations_count}')
            orders = []
            for client in random.sample(clients, k=int(clients_count/10)):
                for product in client.products.all():
                    quantity = random.randint(1,
                                              product.clientproduct_set.
                                              get(client=client).quantity)
                    warehouse_candidates = [wp.warehouse for wp in product.
                                            warehouseproduct_set.all() if wp.
                                            limit >= quantity and wp.
                                            warehouse not in client.order_set.
                                            values_list('warehouse',
                                                        flat=True)]
                    if warehouse_candidates:
                        warehouse = random.choice(warehouse_candidates)
                        distance = random.uniform(10, 1000)
                        orders.append(Order(
                            client=client,
                            warehouse=warehouse,
                            product=product,
                            quantity=quantity,
                            distance=distance
                        ))
            Order.objects.bulk_create(orders)
        self.stdout.write(self.style.
                          SUCCESS('Маркеты сгенерированы успешно!!'))
