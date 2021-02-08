import random

import pyglet

from treecat.note import NoteStatus, Note
from treecat.numberlabel import NumberLabel
from treecat.resources import note_frames_sequence, note_assets_sequence, note_hits_sequence


class PlayerTrough(pyglet.sprite.Sprite):

    def __init__(self, player, start_interval, end_interval, increase_rate, *args, **kwargs):
        self.player = player
        self.missed_margin = 684
        self.overlap_start = 620
        image = pyglet.image.load('assets/images/playertrough.png')
        super().__init__(image, *args, **kwargs)

        self.frames = [
            pyglet.sprite.Sprite(note_frames_sequence[0], x=self.x + 7, y=self.y + self.overlap_start - 15),
            pyglet.sprite.Sprite(note_frames_sequence[1], x=self.x + 107, y=self.y + self.overlap_start - 15),
            pyglet.sprite.Sprite(note_frames_sequence[2], x=self.x + 207, y=self.y + self.overlap_start - 15),
            pyglet.sprite.Sprite(note_frames_sequence[3], x=self.x + 307, y=self.y + self.overlap_start - 15)
        ]
        self.end_interval = end_interval
        self.start_interval = start_interval
        self.interval = start_interval
        self._interval_rem = start_interval
        self.increase_rate = increase_rate
        self.notes = []
        self.combo = 0
        self.score = 0
        self.combo_label = NumberLabel(0, x=1900, y=1000)
        self.score_label = NumberLabel(0, x=1900, y=900)

    def draw(self):
        super().draw()
        for note in self.notes:
            if note.status == NoteStatus.RUNNING and note.y > self.x + self.missed_margin:
                note.missed()
                self.player.miss()
                self.combo = 0
            note.draw()
        for frame in self.frames:
            frame.draw()
        self.combo_label.draw()
        self.score_label.draw()

    def act(self, dt):
        self.player.act(dt)
        living_notes = []
        self._interval_rem -= dt
        if self.interval > self.end_interval:
            self.interval -= (self.interval - self.end_interval) * self.increase_rate * dt
            if self.interval < self.end_interval:
                self.interval = self.end_interval
        if self._interval_rem <= 0:
            self._interval_rem += self.interval
            note_x = random.randint(0, 3)
            note_image = note_assets_sequence[note_x]
            hit_image = note_hits_sequence[note_x]
            interval_range = self.start_interval - self.end_interval
            new_note = Note(note_image, hit_image, 175 + 75 * (1 - (self.interval - interval_range) / self.interval), lifespan=3.5,
                            x=self.x + (100 * note_x) + 16, y=self.y + 10)
            living_notes.append(new_note)
            if random.random() <= 0.05:
                second_note_x = random.randint(0, 3)
                second_note_image = note_assets_sequence[second_note_x]
                second_hit_image = note_hits_sequence[note_x]
                if second_note_x == note_x:
                    second_note_x = note_x + 4 % 4
                new_note = Note(second_note_image, second_hit_image, 175 + 75 * (1 - (self.interval - interval_range) / self.interval),
                                lifespan=3.5,
                                x=self.x + (100 * second_note_x) + 16, y=self.y + 10)
                living_notes.append(new_note)

        for note in self.notes:
            note.act(dt)
            if note.status != NoteStatus.EXPIRED:
                living_notes.append(note)
        self.notes = living_notes
        self.combo_label.value = self.combo

    def press(self, trough_id):
        filter_func = lambda x: x.status == NoteStatus.RUNNING
        note_hit = False
        interval_range = self.start_interval - self.end_interval
        for note in filter(filter_func, reversed(self.notes)):
            if note.y < self.y + self.overlap_start:
                if note.y > self.y + 500 and (note.x - self.x - 16) // 100 == trough_id:
                    note_hit = True
                    self.player.hit()
                    basescore = 5
                    if 260 < note.y < 270:
                        basescore = 10
                        note.perfect()
                        self.combo += 1
                    else:
                        note.hit()
                        self.combo += 1

                    self.score += int(self.combo * basescore * (1 - (self.interval - interval_range) / self.interval))
                    self.score_label.value = self.score
            else:
                note.missed()
                self.player.miss()
                self.combo = 0
        if not note_hit:
            self.combo = 0

    def release(self, trough_id):
        pass