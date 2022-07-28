from client import Client
from product import Product
from orderiterator import OrderIterator

class Cart:
    count = 1

    def __init__(self, client):
        if not isinstance(client, Client):
            raise TypeError("Клиент должен быть инстансом класса Client")

        self.id = Cart.count
        Cart.count += 1
        self.info_client = str(client)
        self.info_product = []

    def __str__(self):
        list_product = "\n".join(map(str, self.info_product))
        return f"Заказ №{self.id} на {self.info_client}:\n\n{list_product}\nСуммарная стоимость: {self.total_cost()}"

    def __iter__(self):
        return OrderIterator(self.info_product)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start < 0 or index.stop > len(self.info_product):
                raise IndexError
            else:
                result = []
                start = 0 if not index.start else index.start
                stop = len(self.info_product) if not index.stop else index.stop
                step = 1 if not index.step else index.step
                for i in range(start, stop, step):
                    result.append(str(self.info_product[i]))
                return result

        if isinstance(index, int):
            if index > len(self.info_product):
                raise IndexError
            else:
                return self.info_product[index]

        raise TypeError()

    def push_product(self, product):
        if isinstance(product, Product):
            self.info_product.append(product)
        else:
            return None

    def delete_product(self, product):
        if not isinstance(product, Product):
            return None
        if product in self.info_product:
            self.info_product.remove(product)
        else:
            return None

    def total_cost(self):
        total_cost = 0
        for item in self.info_product:
            total_cost += item.price
        return total_cost