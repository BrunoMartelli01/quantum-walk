import turtle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from Turtle import Ball
nMove =4
space_lenght = 9
space_high = 15
rows=30
circles =  []
x = range(rows)
y = np.zeros(rows)
startpos = (0, 220)
np.random.seed(0)
def setup_classic(screen, ax ):

    print('setup')
    print(a)
    circles.clear()

    screen.clearscreen()
    global y
    y = np.zeros(rows)
    ax.clear()
    plot.draw()
    screen.tracer(0)


    t = turtle.Turtle()
    global startpos
    startpos = (0, 220, [0,1])
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
        pos = circles
    screen.update()

    # draw_circle((pos[0]+6, pos[1]-10),t)
    # draw_circle((pos[0] -6 , pos[1]- 10), t)





def setup_quantum(screen, ax, ):
    print('setup')
    screen.clearscreen()
    ax.clear()
    circles.clear()
    global y
    global rows
    y = np.zeros(rows)
    plot.draw()
    screen.tracer(0)


    t = turtle.Turtle()

    startpos = (0, 220, np.zeros(nMove))
    startpos[2][0] = 1
    draw_circle1((startpos[0],startpos[1]), t)
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
                pos.append((circle[0] - space_lenght, circle[1] - space_high, np.roll(circles[i-1][0][2], 1)))
                draw_circle1((circle[0] - space_lenght, circle[1] - space_high), t)
            else:

                concl = np.roll(left,-1)
                concr = np.roll(right,1)
                conc = concl+ concr

                pos.append((circle[0] - space_lenght, circle[1] - space_high, conc))
                draw_circle1((circle[0] - space_lenght, circle[1] - space_high), t)



        pos.append((circle[0] + space_lenght, circle[1] - space_high, np.roll(circles[i-1][lenght-1][2],-1)))
        draw_circle1((circle[0] + space_lenght, circle[1] - space_high), t)

        # print(pos)
        # print("-------------------")

        circles.append(pos)

    results = []
    for row in circles:
         sum = 0

         result_list = []
         for circle in row:
             element = np.array(circle[2])
             p = pow(element.sum(),2)
             result_list.append(p)
             sum += p
         results.append(result_list/sum)
    circles.clear()

    for row  in results:
        lenght = len(row)
        sum = 0
        line = []
        for i in range(lenght-1):

            if i == 0:
                line.append((0, 0, [0, row[i]]))
            else:
                line.append((0, 0, [sum, row[i]+sum]))
            sum += row[i]
        line.append((0, 0, [sum, 1]))
        circles.append(line)
    print(circles)

    screen.update()


def draw_circle(pos, t):
    t.penup()

    t.setpos(pos)
    t.color("red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.hideturtle()

def draw_circle1(pos, t):
    t.penup()

    t.setpos(pos)
    t.color("green")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.hideturtle()



def start(screen,ax):
    balls = []
    pos = circles
    print(pos)
    nballs = 500
    print(startpos)
    for k in range(nballs):
        if k < nballs-rows:
                ball= Ball(screen, (startpos[0], startpos[1]))
                balls.append(ball)

        for i in range(0, len(balls)):
                # print(pos[balls[i].depth][balls[i].where][2][0], pos[balls[i].depth][balls[i].where][2][1],balls[i].random)
                if balls[i].random >= pos[balls[i].depth][balls[i].where][2][0] and balls[i].random < pos[balls[i].depth][balls[i].where][2][1]:

                    #move(screen, startpos, True, t)
                    balls[i].isLeft =True
                    balls[i].temp = (balls[i].p[0]-space_lenght, balls[i].p[1]-space_high)
                    balls[i].depth += 1


                else:
                    #move(screen,  startpos, False, t)
                    balls[i].where += 1
                    balls[i].isLeft = False
                    balls[i].temp = (balls[i].p[0]+ space_lenght, balls[i].p[1]-space_high)

                    balls[i].depth += 1

        # print("---------------------------------------------------")


        frame = 5

        for i in range(frame):
            screen.tracer(0)

            for l in range(0, len(balls)):
                #[print(balls[l].p, balls[l].isLeft, balls[l].random)
                move(frame, i, balls[l].p, balls[l].isLeft, balls[l].t)
            screen.update()

        j = 0
        all_balls = True
        while all_balls:
            if j == len(balls):
                all_balls = False

            elif balls[j].depth == rows:
                update_plot(balls[j].where, ax)
                balls.pop(j).t.clear()
            else:
                balls[j].p = balls[j].temp
                j += 1



# pos[0] = (startpos[0]+ space_lenght, startpos[1] - space_high)


def move(frame,i, p, isleft, t):

    moveH = space_high*i /frame
    moveL = space_lenght*i / frame
    t.clear()
    t.penup()
    if isleft:
        t.setpos(p[0] - moveL, p[1] - moveH)
    else:
        t.setpos(p[0] + moveL, p[1] - moveH)
    t.color("Blue")
    t.begin_fill()
    t.circle(7)
    t.end_fill()



def update_plot(pos,ax):
    ax.clear()
    y[pos] += 1
    ax.bar(x, y)
    plot.draw()

if __name__ == '__main__':
    screen = turtle.Screen()
    a = np.array([1, 2, 3, 4])
    b= np.array([1, 2, 3, 4])

    a = np.roll(a, -1)

    print(pow( b.sum(), 2))
    fig = plt.figure(figsize=(12, 5), dpi=80)
    ax = fig.subplots()
    screen.setup(width=1000, height=1000)
    canvas = screen.getcanvas()
    master = canvas.master
    plot = FigureCanvasTkAgg(fig, master=master)




    scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.pack()



    frame = tk.Frame(master)
    frame.pack(side=tk.TOP)

    a =[]
    button = tk.Button(master, text="Classic", command=lambda: setup_classic(screen, ax))

    button.pack(in_=frame, side=tk.RIGHT, padx=10)
    t= turtle.Turtle()

    button2 = tk.Button(master, text="start", command=lambda: start(screen, ax))
    button2.pack(in_=frame, side=tk.RIGHT , padx=10)
    button3 = tk.Button(master, text="Quantum", command=lambda: setup_quantum(screen, ax))
    button3.pack(in_=frame, side=tk.RIGHT, padx=10)

    plot.get_tk_widget().pack(side=tk.BOTTOM)
    # setup(screen, ax)
    master.mainloop()
    screen.exitonclick()
