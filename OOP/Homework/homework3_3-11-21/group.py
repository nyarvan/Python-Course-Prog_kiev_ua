from student import Student
from exception import InputErrorGroup

class Group(Student):
    сount = 1

    def __init__(self):
        self.group = []
        self.count = Group.сount
        Group.сount += 1

    def __str__(self):
        list_group = ""
        for item in self.group:
            list_group += str(item) + "\n"
        return f"Группа №{self.count}:\n{list_group}"

    def push_student(self, student):
        if not (isinstance(student, Student) and student not in self.group):
            return None
        if not len(self.group) < 10:
            raise InputErrorGroup(self.group, f"В группе №{self.count} не может быть больше 10 студентов")
        else:
            self.group.append(student)

    def delete_student(self, student):
        if isinstance(student, Student) and student in self.group:
            self.group.remove(student)
        else:
            return None

    def search_student(self, surname):
        if isinstance(surname, str) and surname.isalpha():
            for item in self.group:
                    if item.surname == surname:
                        return item
        else:
            return None