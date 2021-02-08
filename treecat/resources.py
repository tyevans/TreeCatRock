import pyglet
base_path = ""

note_image = pyglet.image.load('assets/images/note.png')
note_hit_image = pyglet.image.load('assets/images/note_hit.png')
note_perfect_image = pyglet.image.load('assets/images/note_perfect.png')
perfect_react_image = pyglet.image.load('assets/images/lamondemon.png')
good_react_image = pyglet.image.load('assets/images/greencheck.png')
miss_react_image = pyglet.image.load('assets/images/note_missed.png')

number_sheet_image = pyglet.image.load('assets/images/numbers.png')
number_images = pyglet.image.ImageGrid(number_sheet_image, 1, 10)

pawlins_image = pyglet.image.load('assets/images/pawlins_assets.png')
pawlins_sequence = pyglet.image.ImageGrid(pawlins_image, 2, 2)

note_assets_image = pyglet.image.load('assets/images/notes_assets.png')
note_assets_sequence = pyglet.image.ImageGrid(note_assets_image, 1, 4)

note_frames_image = pyglet.image.load('assets/images/notes_frames.png')
note_frames_sequence = pyglet.image.ImageGrid(note_frames_image, 1, 4)

note_hits_image = pyglet.image.load('assets/images/notes_hit.png')
note_hits_sequence = pyglet.image.ImageGrid(note_hits_image, 1, 4)

background_image = pyglet.image.load('assets/images/background.png')
background = pyglet.sprite.Sprite(background_image, x=0, y=0)

nyarson_foe_image = pyglet.image.load('assets/images/nyarson_foe.png')
nyarson_foe_sequence = pyglet.image.ImageGrid(nyarson_foe_image, 2, 2)