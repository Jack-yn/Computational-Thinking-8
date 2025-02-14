#setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
stage.disable_ceiling()
stage.set_background("kitchen")
player = codesters.Sprite("cookie1")
object_speed = -1
player.set_size(0.6)
chips_caught = 0


#objects
def falling_object():
    global object_speed, chips_caught

    if chips_caught < 20:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("chips", x_position, 250)
        object.set_size(0.12)
        object.set_y_speed(object_speed)

stage.event_interval(falling_object,4)

#collision
def collision(player, object):
    global chips_caught

    if object.get_image_name() == "chips":
        stage.remove_sprite(object)
        chips_caught += 1
        if chips_caught > 19:
            player.say(f"you win!", 5)
            stage.set_background("green") 
        else:
            player.say(f"{chips_caught} caught", 0.5)

player.event_collision(collision)

#controls

#right key
def go_right():
    player.move_right(10)

player.event_key("right", go_right)

#left key
def go_left():
    player.move_left(10)

player.event_key("left", go_left)
    