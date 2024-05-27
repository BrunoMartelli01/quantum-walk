import turtle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

space_lenght = 9
space_high = 15
rows=30
x = range(rows)
y = np.zeros(rows)
def setup(screen, ax, circles, ):
    print('setup')
    screen.clearscreen()
    ax.clear()
    plot.draw()
    screen.tracer(0)


    t = turtle.Turtle()
    startpos = (0, 320, [0,1])
    draw_circle((startpos[0],startpos[1]), t)
    circles.append([startpos])

    for i in range(1, rows):

        pos = []
        lenght = len(circles[i - 1])
        for k in range(lenght):
            circle = circles[i - 1][k]
            left = circles[i - 1][k - 1][2]
            right = circle[2]
            # calculate the prob from the father node


            if k == 0:
                pos.append((circle[0] - space_lenght, circle[1] - space_high, [0, (right[0] + right[1]) / 2]))
                draw_circle((circle[0] - space_lenght, circle[1] - space_high), t)
            else:
                pos.append((circle[0] - space_lenght, circle[1] - space_high,[(left[0] + left[1]) / 2, (right[0] + right[1]) / 2]))
                draw_circle((circle[0] - space_lenght, circle[1] - space_high), t)



        pos.append((circle[0] + space_lenght, circle[1] - space_high, [(circles[i - 1][lenght - 1][2][0]+ circles[i - 1][lenght- 1][2][1])/ 2, 1]))
        draw_circle((circle[0] + space_lenght, circle[1] - space_high), t)
        # print(pos)
        # print("-------------------")
        circles.append(pos)

    screen.update()

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




def start(screen, pos,ax, t):
    balls = []
    for k in range(100):
        startpos = (pos[0][0][0], pos[0][0][1])

        t.penup()
        random = np.random.rand()
        # random =0.000000000005
        print(random)
        screen.tracer(0)
        t.setpos(startpos)
        t.color("Blue")
        t.begin_fill()
        t.circle(7)
        t.end_fill()
        t.hideturtle()
        screen.update()

        where = 0

        for i in range(1, len(pos)):

                if random >= pos[i][where][2][0] and random <= pos[i][where][2][1]:

                    move(screen, startpos, True, t)
                    startpos = (pos[i][where][0], pos[i][where][1])

                else:
                    move(screen,  startpos, False, t)
                    where += 1
                    startpos = (pos[i][where][0], pos[i][where][1])

        t.clear()
        print(where)
        update_plot(where, ax)
   # pos[0] = (startpos[0]+ space_lenght, startpos[1] - space_high)


def move(screen, startpos, isleft, t):
    moveH = 0
    moveL = 0
    frame = 20

    for i in range(frame):
        t.clear()
        moveH += space_high / frame
        moveL += space_lenght / frame
        if isleft:
            t.setpos(startpos[0] - moveL, startpos[1] - moveH)
        else:
            t.setpos(startpos[0] + moveL, startpos[1] - moveH)
        t.color("Blue")
        t.begin_fill()
        t.circle(7)
        t.end_fill()
        screen.update()

def update_plot(pos,ax):
    ax.clear()
    y[pos] += 1
    ax.bar(x, y)
    plot.draw()

if __name__ == '__main__':
    screen = turtle.Screen()
    fig = plt.figure(figsize=(12, 3), dpi=80)
    ax = fig.subplots()
    screen.setup(width=1000, height=1000)
    canvas = screen.getcanvas()
    master = canvas.master
    plot = FigureCanvasTkAgg(fig, master=master)




    scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()



    frame = tk.Frame(master)
    frame.pack(side=tk.TOP)
    pos = []
    a =[]
    button = tk.Button(master, text="Setup", command=lambda: setup(screen, ax, pos))

    button.pack(in_=frame, side=tk.RIGHT, padx=10)
    t= turtle.Turtle()

    button2 = tk.Button(master, text="start", command=lambda: start(screen, pos, ax, t))
    button2.pack(in_=frame, side=tk.RIGHT , padx=10)



    plot.get_tk_widget().pack(side=tk.BOTTOM)
    # setup(screen, ax)
    master.mainloop()
    screen.exitonclick()
