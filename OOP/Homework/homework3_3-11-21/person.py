class Person:
    def __init__(self, surname, name, patronymic, age):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str) \
                or not isinstance(age, int):
            raise TypeError("Проверьте введенные значения! Фамилия, имя и отчество - в строковой форме, "
                             "возраст в числовой форме")
        if not surname.isalpha() or not name.isalpha() or not patronymic.isalpha():
            raise ValueError("Проверьте введенные значения! Примечание. Значения состоят только из букв")
        if not 16 < age < 100:
            raise ValueError("Проверьте значение возраста!")

        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        return f"{self.surname} {self.name[0]}.{self.patronymic[0]} {self.age} лет."