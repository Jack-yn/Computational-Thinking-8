###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1=codesters.Square(100, 100, 200, 'blue')
q2=codesters.Square(-100, 100, 200, 'navy')
q3=codesters.Square(-100, -100, 200, 'lightblue')
q4=codesters.Square(100, -100, 200, 'grey')

s1=codesters.Sprite("basketball.jpg", -100, 100)
s1.set_size(0.2)
s2=codesters.Sprite("running-track-field-icon-on-white-background-big-stadium-have-running-track-flat-style-vector.jpg", -100, -100)
s2.set_size(0.3)
s3=codesters.Sprite("dog", 100, -100)
s3.set_size(0.2)
s4=codesters.Sprite("cardinal", 100, 100)
s4.set_size(1)

message1=codesters.Text ("Jack Nowka", 0, 220)
message2=codesters.Text ("I Like Coding", 0, -220)