import turtle
import numpy as np
class Ball:
    t = turtle.Turtle()
    where = 0
    depth = 0
    p = (0, 320)
    temp = ()
    isLeft = False
    random = np.random.rand()
    def __init__(self, screen,startpos=(0, 320)):
        screen.tracer(0)
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.setpos(startpos)
        self.t.color("Blue")
        self.t.begin_fill()
        self.t.circle(7)
        self.t.end_fill()
        self.t.hideturtle()
        self.p = startpos
        screen.update()
        self.random = np.random.rand()
        self.where = 0
        self.depth = 1