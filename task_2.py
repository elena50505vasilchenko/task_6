class Road:

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        total = self._length * self._width * self.weight * self.depth / 1000
        print(f'Масса асфальта - {int(total)} т')


r = Road(20, 5000, 25, 5)
r.mass()
