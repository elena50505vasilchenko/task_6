class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        """Разгоняется"""
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        """Останавливается"""
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        """Поворачивается"""
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Стоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def test(auto):
    print(f"Автомобиль {auto.name}, цвет {auto.color}")
    auto.go(80)
    auto.show_speed()
    auto.turn('направо')
    auto.stop()
    auto.show_speed()
    auto.turn('налево')
    auto.go(30)
    auto.show_speed()
    auto.go(60)
    auto.show_speed()
    auto.stop()


car = Car(0, 'белый', 'Honda', False)
test(car)

car_1 = TownCar(0, 'коричневый', 'Volkswagen', True)
test(car_1)

car_2 = SportCar(0, 'желтый', 'Lamborghini', False)
test(car_2)

car_3 = WorkCar(0, 'красный', 'Audi', True)
test(car_3)

car_4 = PoliceCar(0, 'синий', 'Ford', False)
test(car_4)
