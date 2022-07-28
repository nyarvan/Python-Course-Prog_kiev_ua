from person import Person

class Student(Person):
    def __init__(self, surname, name, patronymic, age, course, speciality, university):
        if not isinstance(course, int) or not isinstance(speciality, str) or not isinstance(university, str):
            raise TypeError("Проверьте введенные значения!")
        if not 0 < course < 7:
            raise ValueError("Проверьте введенный курс!")

        super().__init__(surname, name, patronymic, age)
        self.course = course
        self.speciality = speciality
        self.university = university

    def __str__(self):
        return f"{super().__str__()}\nУчиться в {self.university} на {self.course} курсе, " \
               f"на специальности {self.speciality}."