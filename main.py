import turtle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def setup(screen, ax, ipos, rows=43, ):
    print('setup')
    screen.clearscreen()
    ax.clear()
    plot.draw()
    screen.tracer(0)

    space_lenght = 9
    space_high = 15
    t = turtle.Turtle()
    startpos = (9, 335)
    circles = [[startpos]]
    for i in range(1, rows):

        pos = []
        for circle in circles[i - 1]:
            draw_circle((circle[0] - space_lenght, circle[1] - space_high), t)
            # print(circle[0]- space_lenght, circle[1]-space_high)
            pos.append((circle[0] - space_lenght, circle[1] - space_high))

        # draw_circle((pos[-1][0]+ 6, pos[-1][1]-10), t)
        pos.append((pos[-1][0] + 2 * space_lenght, pos[-1][1]))
        # print(pos)
        # print("-------------------")
        circles.append(pos)

    screen.update()

    ipos.append( circles)
    # draw_circle((pos[0]+6, pos[1]-10),t)
    # draw_circle((pos[0] -6 , pos[1]- 10), t)


def draw_circle(pos, t):
    t.penup()

    t.setpos(pos)
    t.color("red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.hideturtle()
def start(screen):
    startpos = (0, 320)
    t = turtle.Turtle()
    t.penup()

    t.setpos(startpos)
    t.color("Blue")
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.hideturtle()

if __name__ == '__main__':
    screen = turtle.Screen()
    fig = plt.figure(figsize=(12, 3), dpi=80)
    ax = fig.subplots()
    screen.setup(width=1000, height=1000)
    canvas = screen.getcanvas()
    master = canvas.master
    plot = FigureCanvasTkAgg(fig, master=master)
    x = np.random.randint(0, 43, 100)
    y = np.random.randint(0, 43, 100)
    print(x, y)
    ax.bar(x, y)

    plot.draw()
    scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()



    frame = tk.Frame(master)
    frame.pack(side=tk.TOP)
    pos =[]
    button = tk.Button(master, text="Setup", command=lambda: setup(screen, ax, pos))
    print(pos)
    button.pack(in_=frame, side=tk.RIGHT, padx=10)
    button2 = tk.Button(master, text="start", command=lambda: start(screen))
    button2.pack(in_=frame, side=tk.RIGHT , padx=10)



    plot.get_tk_widget().pack(side=tk.BOTTOM)
    # setup(screen, ax)
    master.mainloop()
    screen.exitonclick()
