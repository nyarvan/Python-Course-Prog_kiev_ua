class Client:
    def __init__(self, surname, name, patronymic, phone):
        if not (isinstance(surname, str) or isinstance(name, str) or isinstance(patronymic, str)):
            raise TypeError("Фамилия и имя должны быть строкой!")
        if not isinstance(phone, str):
            raise TypeError("Номер телефона должен быть строкой!")
        if not surname.isalpha():
            raise ValueError("Фамилия должна состоять только из букв!")
        if not name.isalpha():
            raise ValueError("Имя должно состоять только из букв!")
        if not patronymic.isalpha():
            raise ValueError("Отчество должно состоять только из букв!")
        if phone.isalpha():
            raise ValueError("Неверный формат номера телефона!")

        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f"Клиент {self.surname} {self.name[0]}.{self.patronymic[0]} тел.: {self.phone}"
