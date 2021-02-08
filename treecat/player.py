import pyglet

from treecat.resources import pawlins_sequence, nyarson_foe_sequence


class Pawlins(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        self.anim_pause = .25
        self._anim_pause = self.anim_pause
        self.is_idle = True
        super().__init__(pawlins_sequence[2], *args, **kwargs)

    def set_pose_timeout(self):
        self._anim_pause = self.anim_pause

    def act(self, dt):
        self._anim_pause -= dt
        if not self.is_idle and self._anim_pause <= 0:
            self.idle()

    def idle(self):
        self.is_idle = True
        self.image = pawlins_sequence[2]

    def hit(self):
        self.set_pose_timeout()
        self.is_idle = False
        self.image = pawlins_sequence[3]

    def miss(self):
        self.set_pose_timeout()
        self.is_idle = False
        self.image = pawlins_sequence[1]

    def sad_idle(self):
        self.set_pose_timeout()
        self.is_idle = True
        self.image = pawlins_sequence[0]

class NyarsonFoe(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        self.anim_pause = .25
        self._anim_pause = self.anim_pause
        self.is_idle = True
        super().__init__(nyarson_foe_sequence[2], *args, **kwargs)

    def set_pose_timeout(self):
        self._anim_pause = self.anim_pause

    def act(self, dt):
        self._anim_pause -= dt
        if not self.is_idle and self._anim_pause <= 0:
            self.idle()

    def idle(self):
        self.is_idle = True
        self.image = nyarson_foe_sequence[2]

    def hit(self):
        self.set_pose_timeout()
        self.is_idle = False
        self.image = nyarson_foe_sequence[3]

    def miss(self):
        self.set_pose_timeout()
        self.is_idle = False
        self.image = nyarson_foe_sequence[1]

    def sad_idle(self):
        self.set_pose_timeout()
        self.is_idle = True
        self.image = nyarson_foe_sequence[0]


class RivalPair:

    def __init__(self, player, rival):
        self.player = player
        self.rival = rival

    def act(self, dt):
        self.player.act(dt)
        self.rival.act(dt)

    def draw(self):
        self.player.draw()
        self.rival.draw()

    def idle(self):
        self.player.idle()
        self.rival.idle()

    def hit(self):
        self.player.hit()
        self.rival.miss()

    def miss(self):
        self.player.miss()
        self.rival.hit()

    def sad_idle(self):
        self.player.sad_idle()
        self.rival.hit()
