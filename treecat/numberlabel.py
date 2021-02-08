import pyglet

from treecat.resources import number_images


class NumberLabel():
    _value = 0
    def __init__(self, value, x:int, y:int):
        self.x = x
        self.y = y
        self.children = []
        self.scale = .5
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        spacing = 64
        _v = str(value)
        offset = self.x - (len(_v) * spacing)
        children = []

        for i, n in enumerate(str(self.value)):
            child = pyglet.sprite.Sprite(number_images[int(n)], x=offset + spacing * i, y=self.y)
            child.scale = self.scale
            children.append(child)
        self.children = children
        self._value = value

    def draw(self):
        for child in self.children:
            child.draw()