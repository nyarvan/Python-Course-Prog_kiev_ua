from order import Order
from cart import Cart
from product import Product
from client import Client

if __name__ == "__main__":
    """
    x = Order('xxx', 10, 20)
    print(x.get_price())
    """
    ivan_rybak = Client("Рыбак", "Ivan", "Andrievich", "+380667899504")
    iphone12 = Product("Iphone12", 22999.99, "abd", "ffoflfl")
    print(iphone12.price)
    iphone12.price = "axaxax"
    print(iphone12)

