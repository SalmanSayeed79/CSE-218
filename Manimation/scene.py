from manim import *

#manim -pql scene.py CreateCircle
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        square=Square()
        square.set_fill(RED,opacity=0.5)# create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))
        self.play(Transform(circle,square))# show the circle on screen