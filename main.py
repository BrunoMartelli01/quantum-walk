
import turtle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
def setup(screen,ax, rows = 5):
    print('setup')
    screen.clearscreen()
    ax.clear()
    t = turtle.Turtle()
    pos = (0,100)
    draw_circle(pos, t)
def draw_circle(pos, t):
    t.penup()
    t.speed(1000)
    t.setpos(pos)
    t.color("black", "red")
    t.begin_fill()
    t.circle(3)
    t.end_fill()


if __name__ == '__main__':
    screen = turtle.Screen()
    fig = plt.figure(figsize=(4, 3), dpi=80)
    ax = fig.subplots()
    screen.setup(width=1000, height=1000)
    canvas = screen.getcanvas()
    master = canvas.master
    plot = FigureCanvasTkAgg(fig, master=master)
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    print(x, y)
    ax.bar(x, y)
    plot.draw()
    scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()
    plot.get_tk_widget().pack()
    setup(screen, ax)
    master.mainloop()
    screen.exitonclick()