import pyglet

from treecat.resources import perfect_react_image, good_react_image, miss_react_image


class PerfectReact(pyglet.sprite.Sprite):
    def __init__(self, speed=400, *args, **kwargs):
        self.speed = speed
        super().__init__(perfect_react_image, *args, **kwargs)

    def act(self, dt):
        self.y += self.speed * dt


class GoodReact(pyglet.sprite.Sprite):
    def __init__(self, speed=400, *args, **kwargs):
        self.speed = speed
        super().__init__(good_react_image, *args, **kwargs)

    def act(self, dt):
        self.y += self.speed * dt


class MissReact(pyglet.sprite.Sprite):
    def __init__(self, speed=200, *args, **kwargs):
        self.speed = speed
        super().__init__(miss_react_image, *args, **kwargs)

    def act(self, dt):
        self.y += self.speed * dt
