from Student import Student

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
        if isinstance(student, Student) and student not in self.group:
            self.group.append(student)
        else:
            return None

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


