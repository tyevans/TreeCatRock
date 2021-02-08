from enum import Enum

import pyglet

from treecat.reaction import MissReact, PerfectReact, GoodReact


class NoteStatus(Enum):
    RUNNING = 0
    EXPIRED = 1
    HIT = 2
    MISSED = 3


class Note(pyglet.sprite.Sprite):
    def __init__(self, image, hit_image, speed, lifespan=3.0, *args, **kwargs):
        self.hit_image = hit_image
        self.speed = speed
        self.status = NoteStatus.RUNNING
        self.ttl = lifespan
        self.expired = False
        self.react_child = None
        super().__init__(image, *args, **kwargs)

    def act(self, dt):
        self.y += self.speed * dt
        self.ttl -= dt
        if self.ttl <= 0:
            self.status = NoteStatus.EXPIRED
        else:
            if self.react_child:
                self.react_child.act(dt)

    def draw(self):
        super().draw()
        if self.react_child:
            self.react_child.draw()

    def hit(self):
        self.status = NoteStatus.HIT
        self.image = self.hit_image
        self.react_child = GoodReact(x=self.x + 16, y=self.y)

    def perfect(self):
        self.status = NoteStatus.HIT
        self.image = self.hit_image
        self.react_child = PerfectReact(x=self.x + 16, y=self.y)

    def missed(self):
        self.status = NoteStatus.MISSED
        self.react_child = MissReact(x=self.x, y=self.y)