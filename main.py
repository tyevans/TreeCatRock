import pyglet
from pyglet.window import key

from treecat.board import PlayerTrough
from treecat.player import Pawlins, NyarsonFoe, RivalPair
from treecat.resources import background

window = pyglet.window.Window(1920, 1080, fullscreen=False)

pawlins = Pawlins(x=1400, y=180)
nyarson_foe = NyarsonFoe(x=256, y=180)
rival_pair = RivalPair(pawlins, nyarson_foe)
trough = PlayerTrough(rival_pair, .5, 0.3, 0.01, x=1003, y=334)


@window.event
def on_draw():
    window.clear()
    background.draw()
    trough.draw()
    rival_pair.draw()


def update(dt):
    trough.act(dt)


key_troughs = {
    key.A: 0,
    key.S: 1,
    key.D: 2,
    key.F: 3,
}


@window.event
def on_key_press(symbol, modifiers):
    trough_id = key_troughs.get(symbol)
    if trough is not None:
        trough.press(trough_id)


@window.event
def on_key_release(symbol, modifiers):
    trough_id = key_troughs.get(symbol)
    if trough is not None:
        trough.release(trough_id)


pyglet.clock.schedule_interval(update, 1 / 120.0)
pyglet.app.run()
