class Stationary:
    def __init__(self, title=' '):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        self.title = 'pen'
        print(f'Draws with a {self.title}')


class Pencil(Stationary):

    def draw(self):
        self.title = 'pencil'
        print(f'Draws with a {self.title}')


class Handle(Stationary):

    def draw(self):
        self.title = 'handle'
        print(f'Draws with a {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
