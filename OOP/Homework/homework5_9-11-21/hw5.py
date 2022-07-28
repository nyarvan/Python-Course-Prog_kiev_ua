from group_student.student import Student
from group_student.group import Group
from cart.product import Product
from cart.client import Client
from cart.order import Order

if __name__ == "__main__":
    print("Exercise 1:")
    rybak_ivan = Student("Рыбак", "Иван", "Андреевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    razno_oleg = Student("Разно", "Олег", "Сергеевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    filatov_alexandr = Student("Филатов", "Александр", "Владимирович", 19, 2,
                               "Основы инженерии программного обеспечения", "КПИ")
    chervenko_bogdan = Student("Червенко", "Богдан", "Владимирович", 18, 2, "Основы инженерии программного обеспечения",
                               "КПИ")
    vashchuk_alexandr = Student("Ващук", "Александр", "Максимович", 19, 2, "Основы инженерии программного обеспечения",
                                "НАУ")
    osipov_artem = Student("Осипов", "Артем", "Александрович", 19, 2, "Кибербезпека", "НАУ")

    group1 = Group()
    group1.push_student(rybak_ivan)
    group1.push_student(razno_oleg)
    group1.push_student(vashchuk_alexandr)
    group1.push_student(osipov_artem)
    print(group1, "\n")
    print("\nОбращение по индексу:")
    print(group1[2], "\n")
    print("Результат роботы итератора:")
    for student in group1:
        print(student)

    print("\nExercise 2:")
    iphone12 = Product("Iphone 12", 26000, "Смартфон от компании Apple", "Масса: 164 грамм, Размеры: 146,7х71,5х7,4 мм")
    watch = Product("Apple Watch Series 6", 11500, "Смарт-часы от компании Apple",
                    "Масса: 48 г, Размеры: 44×38×10,7 мм")
    airpods_pro = Product("Apple AirPods Pro", 7500, "Безпроводные наушники от компании Apple",
                          "Масса: 45,6 г, Размеры: 60,6 x 45,2 x 21,7 мм")
    rybak_ivan = Client("Рыбак", "Иван", "Андреевич", "+380667899504")
    order1 = Order(rybak_ivan)
    order1.push_product(watch)
    order1.push_product(airpods_pro)
    order1.push_product(iphone12)
    order1.push_product(iphone12)
    order1.push_product(airpods_pro)
    order1.push_product(watch)
    print(order1, "\n")
    print("\nСрез обьектов:")
    print(order1[2:5], "\n")
    print("Результат роботи итератора:")
    for product in order1:
        print(product)
