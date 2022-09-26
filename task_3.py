class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


person = Position('Антон', 'Антонов', 'оператор', 150, 20)
print(f'Работник: {person.get_full_name()}, должность - {person.position}, доход - {person.get_full_salary()}')

