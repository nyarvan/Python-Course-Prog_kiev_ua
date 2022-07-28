from group_student.student import Student
from group_student.groupiterator import GroupIterator

class Group(Student):
    сount = 1

    def __init__(self):
        self.group = []
        self.count = Group.сount
        Group.сount += 1

    def __str__(self):
        list_group = "\n".join(map(str, self.group))
        return f"Группа №{self.count}:\n{list_group}"

    def __iter__(self):
        return GroupIterator(self.group)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start < 0 or index.stop > len(self.group):
                raise IndexError
            else:
                result = []
                start = 0 if not index.start else index.start
                stop = len(self.group) if not index.stop else index.stop
                step = 1 if not index.step else index.step
                for i in range(start, stop, step):
                    result.append(str(self.group[i]))
                return result

        if isinstance(index, int):
            if index > len(self.group):
                raise IndexError
            else:
                return self.group[index]

        raise TypeError()

    def push_student(self, student):
        if not isinstance(student, Student):
            return None
        if student in self.group:
            return None
        self.group.append(student)

    def delete_student(self, student):
        if not isinstance(student, Student):
            return None
        if student not in self.group:
            return None
        self.group.remove(student)

    def search_student(self, surname):
        if not isinstance(surname, str):
            return None
        if not surname.isalpha():
            return None
        for item in self.group:
            if item.surname == surname:
                return item

