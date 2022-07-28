from exception import InputErrorPrice
from exception import InputErrorGroup
from product import Product
from student import Student
from group import Group

if __name__ == '__main__':

    price = input("Введите цену товара: ")
    try:
        iphone12 = Product("Iphone 12", price, "Смартфон от компании Apple", "110 мм х 65 мм")

    except InputErrorPrice as err:
        print(err)
    else:
        print(iphone12)

    rybak_ivan = Student("Рыбак", "Иван", "Андреевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    razno_oleg = Student("Разно", "Олег", "Сергеевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    filatov_alexandr = Student("Филатов", "Александр", "Владимирович", 19, 2,
                               "Основы инженерии программного обеспечения", "КПИ")
    chervenko_bogdan = Student("Червенко", "Богдан", "Владимирович", 18, 2, "Основы инженерии программного обеспечения",
                               "КПИ")
    vashchuk_alexandr = Student("Ващук", "Александр", "Максимович", 19, 2, "Основы инженерии программного обеспечения",
                                "НАУ")
    osipov_artem = Student("Осипов", "Артем", "Александрович", 19, 2, "Кибербезпека", "НАУ")
    korenevski_alexandr = Student("Кореневский", "Александр", "Кирилович", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    sidorenko_vladislav = Student("Сидоренко", "Владислав", "Сергеевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    bondarenko_bogdan = Student("Бондаренко", "Богдан", "Владимирович", 19, 2,
                               "Основы инженерии программного обеспечения", "КПИ")
    bondareva_nikol = Student("Бондарева", "Николь", "Руслановна", 18, 2, "Основы инженерии программного обеспечения",
                               "КПИ")
    shupik_luidmila = Student("Шупик", "Людмила", "Владимировна", 19, 2, "Основы инженерии программного обеспечения",
                                "НАУ")
    kozhevnikov_illya = Student("Кожевников", "Иллья", "Павлович", 19, 2, "Основы инженерии программного обеспечения",
                              "НАУ")
    group1 = Group()
    try:
        group1.push_student(rybak_ivan)
        group1.push_student(razno_oleg)
        group1.push_student(filatov_alexandr)
        group1.push_student(chervenko_bogdan)
        group1.push_student(vashchuk_alexandr)
        group1.push_student(osipov_artem)
        group1.push_student(korenevski_alexandr)
        group1.push_student(sidorenko_vladislav)
        group1.push_student(shupik_luidmila)
        group1.push_student(bondarenko_bogdan)
        group1.push_student(bondareva_nikol)
    except InputErrorGroup as err1:
        print(err1)
    else:
        print(group1)