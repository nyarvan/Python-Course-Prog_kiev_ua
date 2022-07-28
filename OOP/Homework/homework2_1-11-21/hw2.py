from Student import Student
from Group import Group

if __name__ == '__main__':
    rybak_ivan = Student("Рыбак", "Иван", "Андреевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    razno_oleg = Student("Разно", "Олег", "Сергеевич", 18, 2, "Основы инженерии программного обеспечения", "НАУ")
    filatov_alexandr = Student("Филатов", "Александр", "Владимирович", 19, 2, "Основы инженерии программного обеспечения", "КПИ")
    chervenko_bogdan = Student("Червенко", "Богдан", "Владимирович", 18, 2, "Основы инженерии программного обеспечения", "КПИ")
    vashchuk_alexandr = Student("Ващук", "Александр", "Максимович", 19, 2, "Основы инженерии программного обеспечения", "НАУ")
    osipov_artem = Student("Осипов", "Артем", "Александрович", 19, 2, "Кибербезпека", "НАУ")

    group1 = Group()
    group1.push_student(rybak_ivan)
    group1.push_student(razno_oleg)
    group1.push_student(vashchuk_alexandr)
    group1.push_student(osipov_artem)
    print(group1)
    group1.delete_student(osipov_artem)
    print(group1)
    print(group1.search_student("Рыбак"))

    group2 = Group()
    group2.push_student(filatov_alexandr)
    group2.push_student(chervenko_bogdan)
    print("\n")
    print(group2)
    print(group2.search_student("Рыбак"))