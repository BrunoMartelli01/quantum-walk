import turtle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from Turtle import Ball
nMove =4
space_lenght = 9
space_high = 15
rows= 30
circles =  []
x = range(rows)
y = np.zeros(rows)
startpos = (0, 220)
perturbation = 0
delta = 0.1  # perturbazione da sommare alla probabilità
nballs = 2000
def setup_classic(screen, ax ):
    np.random.seed(0)
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
    temp= []
    s = 0
    for i in range(len(circles[-1])):
       # print(circles[-1][i][2][1] - circles[-1][i][2][0])
        temp.append(circles[-1][i][2][1] - circles[-1][i][2][0])


    test(ax, temp)
    screen.update()

    # draw_circle((pos[0]+6, pos[1]-10),t)
    # draw_circle((pos[0] -6 , pos[1]- 10), t)



def perturbate(k,pos, t):
    r = np.random.randint(0, 1000)
    r = r / 1000
    if r < perturbation:
        print(r, perturbation)
        random = np.random.randint(0, 4)
        pos[k][2][random] += delta
        #pos[k][2] [random] = pos[k][2].sum() * delta
        #temp = [pos[k][0], pos[k][1], pos[k][2]]
        temp =  [pos[k][0], pos[k][1],np.roll(pos[k][2], 1)]


        pos[k] = temp
        draw_circle((pos[k][0], pos[k][1]), t)
    return pos


def setup_quantum(screen, ax, ):
    np.random.seed(0)
    print('setup')
    screen.clearscreen()
    ax.clear()


    tot_rows = 0
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
                pos = perturbate( 0, pos,t)

            else:

                concl = np.roll(left,-1)
                concr = np.roll(right,1)
                conc = concl+ concr


                pos.append((circle[0] - space_lenght, circle[1] - space_high, conc))
                draw_circle1((circle[0] - space_lenght, circle[1] - space_high), t)
                pos = perturbate(k,pos, t)




        pos.append((circle[0] + space_lenght, circle[1] - space_high, np.roll(circles[i-1][lenght-1][2],-1)))
        draw_circle1((circle[0] + space_lenght, circle[1] - space_high), t)

        pos = perturbate(lenght,pos, t)
        circles.append(pos)


    results = []
    counter = 0

    counter_row = 0
    list_modyfied = []
    for row in circles:
         sum = 0


         result_list = []

         counter = 0
         for circle in row:
             element = np.array(circle[2])

             # r = np.random.randint(0,1000)
             # r= r/1000
             #
             # if r < perturbation:
             #     print(r, perturbation)
             #     draw_circle((circles[counter_row][counter][0], circles[counter_row][counter][1]), t)
                 # random = np.random.randint(0, 4)
                 # print(element.sum())
                 # s = element.sum()
                 # element[random] += s*delta

                 #element = np.roll(element, 1)



                 # element[random] += pow(delta,i) #qua c'è dove viene sommata la perturbazione
                 #
                 # a = pow(element[0] - element[2], 2)
                 # b = pow(element[1] - element[3], 2)
                 # print(element[random],counter, a+b)



             a = pow(element[0]-element[2],2)
             b = pow(element[1]-element[3],2)
             result_list.append(a+b)
             sum += a+b
             counter += 1
         counter_row += 1

         # result_list = result_list/sum
         # print(result_list)
         # sum = 0
         # for i in range(len(result_list)):
         #     r = np.random.rand()
         #     sum  += result_list[i]
         #     if r < perturbation:
         #         result_list[i] += delta
         #         sum += delta
         #


         # print(result_list/sum,"-----------------------")
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

    test(ax, results[-1])
    # for i in range(len(circles)):
    #     print(circles[i])
    print(circles)

    screen.update()
def test(ax, range):
    ax.clear()
    ax.set_ylim(0, 0.3)
    ax.grid(True)
    ax.bar(x,range)
    plot.draw()
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
    for k in range(nballs):
        if k < nballs-rows:
                ball= Ball(screen, (startpos[0], startpos[1]))
                balls.append(ball)

        for i in range(0, len(balls)):

                balls[i].percorso.append([[pos[balls[i].depth][balls[i].where][2][0], pos[balls[i].depth][balls[i].where][2][1]],balls[i].random])
                #print(balls[i].percorso, balls[i].random)
                #print(pos[balls[i].depth-1][balls[i].where][2][0] , pos[balls[i].depth-1][balls[i].where][2][1],)
                if (balls[i].random < pos[balls[i].depth][balls[i].where][2][1] and pos[balls[i].depth][balls[i].where][2][1]!=1) or (pos[balls[i].depth][balls[i].where][2][1]==1 and balls[i].random < pos[balls[i].depth][balls[i].where][2][0]):

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
                balls[i].percorso.append(balls[i].isLeft)
        #print("---------------------------------------------------")


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
                for i in range(rows):
                    if(pos[rows-1][i][2][0] < balls[j].random < pos[rows-1][i][2][1]):
                        if(balls[j].where != i):
                            print(balls[j].where, i)
                        update_plot(balls[j].where, ax) # I o where I bari  balls[j].where fai vedere dove cadono effetiavmente le palline
                h = balls.pop(j)
                h.t.clear()

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

def set_perturbation(x):
    global perturbation
    perturbation = int(x)/100

def update_plot(pos,ax):
    ax.clear()
    ax.set_ylim(0, 0.3)
    ax.grid(True)
    global y
    y = np.array(y)
    y[pos] += 1
    normalizer = y.sum()
    ax.bar(x, y/normalizer)
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




    scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x:set_perturbation(x))
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
