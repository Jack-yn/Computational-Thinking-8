import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(1)

def move_up(sprite):
    sprite.move_up(10)

def move_right(sprite):
    sprite.move_right(10)

def move_left(sprite):
    sprite.move_left(10)

def move_down(sprite):
    sprite.move_down(10)

def hide(sprite):
    sprite.hide()

def show(sprite):
    sprite.show()

s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s1.event_key("h", hide)
s1.event_key("u", show)

print("Game has started. Open the screen by using PORTS to play")