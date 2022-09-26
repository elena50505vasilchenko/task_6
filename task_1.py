import time


class TrafficLight:
    red = 'красный'
    yellow = 'желтый'
    green = 'зеленый'
    red_color = 7
    yellow_color = 2
    green_color = 4

    def __init__(self, color):
        self.__color = color
        print(f'\nОбъект с цветом - {self.__color}')

    def switch_light(self, color, period):
        self.period = period
        print(f'Включен {color}, на {self.period} сек')
        time.sleep(self.period)

    def running(self, color=''):
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red:
            self.switch_light('красный', self.red_color)
            self.switch_light('желтый', self.yellow_color)
            self.switch_light('зеленый', self.green_color)
        elif loc_color == self.yellow:
            self.switch_light('желтый', self.yellow_color)
            self.switch_light('зеленый', self.green_color)
        else:
            self.switch_light('зеленый', self.green_color)

        print('Цикл завершен')

