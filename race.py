import random
import turtle

racing_turtles = 6                                              # Number of racing turtles
finish_line = 240                                               # How far the turtles have to race to the finish
speed = 20                                                      # The maximum move a turtle makes in a single update
silks = ["red", "blue", "green", "purple", "orange", "salmon"]  # Colours of the turtles
t = []                                                          # List holding each turtle
position = []                                                   # List holding the y position of each turtle
window = turtle.Screen()
window.setup(1000, 600)

winnerdraw = turtle.Turtle()
winorlosedraw = turtle.Turtle()
winorlosedraw.hideturtle()
winorlosedraw.penup()
errordraw = turtle.Turtle()
errordraw.hideturtle()
wincountdraw = turtle.Turtle()
wincountdraw.hideturtle()
wincountdraw.penup()
buttontitledraw = turtle.Turtle()
buttontitledraw.hideturtle()
buttontitledraw.penup()
choicedraw = turtle.Turtle()
choicedraw.penup()
choicedraw.pensize(2)

selectedcol1 = None
raceorreset = 1
racing = False
wincount = 0
gamecount = 0
drawing = True

def draw_buttons() -> None:
    choicedraw.left(90)
    choicedraw.goto(((-racing_turtles * 50) / 2) - 100, -160)
    buttondrawer = turtle.Turtle()
    buttondrawer.penup()
    buttondrawer.pensize(2)
    count = 0
    for i in range(0, racing_turtles):
        buttondrawer.goto(((-racing_turtles * 50) / 2) + count, -100)
        buttondrawer.fillcolor(silks[i])
        buttondrawer.begin_fill()
        buttondrawer.pendown()
        for v in range(1,5):
            buttondrawer.forward(45)
            buttondrawer.right(90)
        buttondrawer.end_fill()
        buttondrawer.forward(45)
        count += 50
        buttondrawer.penup()

    buttondrawer.goto(-125, -200)
    buttondrawer.pendown()
    buttondrawer.fillcolor("Green")
    buttondrawer.begin_fill()
    buttondrawer.goto(125, -200)
    buttondrawer.goto(125, -250)
    buttondrawer.goto(-125, -250)
    buttondrawer.goto(-125, -200)
    buttondrawer.end_fill()
    buttondrawer.penup()
    buttondrawer.goto(((-racing_turtles * 50) / 2) - 100, -100)
    buttondrawer.hideturtle()
    buttontitledraw.goto(-100, -242.5)
    buttontitledraw.write("Start Race", font=("Arial", 20, "bold"))


def on_screen_click(x, y) -> None:
    global selectedcol1
    global raceorreset
    global racing
    global wincount
    global gamecount

    startlocation = (-racing_turtles * 50) / 2

    if startlocation <= x <= startlocation + 45 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[0]
        choicedraw.goto(startlocation + 22.5, -160)

    elif startlocation + 50 <= x <= startlocation + 95 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[1]
        choicedraw.goto(startlocation + 50 + 22.5, -160)

    elif startlocation + 100 <= x <= startlocation + 145 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[2]
        choicedraw.goto(startlocation + 100 + 22.5, -160)

    elif startlocation + 150 <= x <= startlocation + 195 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[3]
        choicedraw.goto(startlocation + 150 + 22.5, -160)

    elif startlocation + 200 <= x <= startlocation + 245 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[4]
        choicedraw.goto(startlocation + 200 + 22.5, -160)

    elif startlocation + 250 <= x <= startlocation + 295 and -145 <= y <= -100 and racing == False:
        errordraw.clear()
        selectedcol1 = silks[5]
        choicedraw.goto(startlocation + 250 + 22.5, -160)
    
    elif -125 <= x <= 125 and -250 <= y <= -200 and raceorreset != 0:
        if raceorreset == 1 and selectedcol1 != None and drawing != True:
            errordraw.clear()
            buttontitledraw.clear()
            buttontitledraw.goto(-100, -242.5)
            buttontitledraw.write("Reset Race", font=("Arial", 20, "bold"))
            raceorreset = 0
            winornowin = race(selectedcol1)
            wincount += winornowin
            gamecount += 1
            raceorreset = 2

            winorlosedraw.goto(((-racing_turtles * 50) / 2) + 75, finish_line + 10)
            if winornowin == 1:
                winorlosedraw.pencolor("Green")
                winorlosedraw.write("YOU WON!", font=("Arial", 20, "bold"))
            else:
                winorlosedraw.pencolor("Red")
                winorlosedraw.write("YOU LOST!", font=("Arial", 20, "bold"))

            wincountdraw.clear()
            wincountdraw.goto(200, -52.5)
            wincountdraw.write(f"{wincount} Wins", font=("Arial", 20, "bold"))
            wincountdraw.goto(200, -82.5)
            wincountdraw.write(f"{gamecount} Games Played", font=("Arial", 20, "bold"))


        elif raceorreset == 1 and selectedcol1 == None and drawing != True:
            errordraw.clear()
            errordraw.penup()
            errordraw.goto(-125, -190)
            errordraw.pencolor("Red")
            errordraw.write("Please pick a colour!", font=("Arial", 20, "bold"))

        elif raceorreset == 2:
            errordraw.clear()
            buttontitledraw.goto(-100, -242.5)
            buttontitledraw.clear()
            buttontitledraw.write("Start Race", font=("Arial", 20, "bold"))
            raceorreset = 0
            reset_race()
            raceorreset = 1

window.onclick(on_screen_click)

def draw_finish_line() -> None:
    winnerdraw.hideturtle()
    winnerdraw.penup()
    winnerdraw.goto(200, finish_line - 50)
    winnerdraw.pendown()
    referee = turtle.Turtle()
    referee.pensize(2)
    referee.penup()
    referee.goto((-racing_turtles * 50) / 2, finish_line)
    referee.pendown()
    referee.forward(racing_turtles * 50)
    referee.penup()
    referee.goto(((-racing_turtles * 50) / 2) - 50, finish_line)

def starters_orders() -> None:
    currentplacement = (-racing_turtles * 50) / 2
    placement = 25

    for indvturtle in t:
        indvturtle.penup()
        indvturtle.goto(currentplacement + placement, 0)
        indvturtle.setheading(90)
        placement += 50
        indvturtle.pendown()

    global drawing
    drawing = False

def race(selectedcol1) -> int: #Returns amount win count should go up.
    global racing
    racing = True
    winner = ""
    now = 0
    winners = []

    for i in silks:
        winners.append("")

    continues = True
    ind = 0
    print("Results:")

    while continues:
        for i, turt in enumerate(t):
            if position[i] != finish_line:
                distance = random.randint(1, speed)
                if position[i] + distance > finish_line:
                    distance = finish_line - position[i]
                turt.forward(distance)
                position[i] += distance
            else:
                col = silks[i]
                if col not in winners:
                    winners[ind] = col
                    ind += 1
                    now += 1
                    print(winners)
                if now == racing_turtles:
                    continues = False

    for i, w in enumerate(winners, start=1):
        print(f"{i} : {w}")

        winnerdraw.pencolor(silks[silks.index(w)])
        winnerdraw.write(f"{i} : {winners[i-1].upper()}", font=("Arial", 20, "bold"))
        x, y = winnerdraw.pos()
        winnerdraw.penup()
        winnerdraw.goto(x, y - 30)
    print(selectedcol1)
    if selectedcol1 == winners[0]:
        print("YOU GUESSED CORRECTLY!")
        return 1
    else:
        print("YOU GUESSED INCORRECTLY!")
        return 0

def reset_race() -> None:
    winorlosedraw.clear()
    winnerdraw.clear()
    winnerdraw.goto(200, finish_line - 50)
    choicedraw.goto(((-racing_turtles * 50) / 2) - 100, -160)
    global selectedcol1
    selectedcol1 = None
    for i, turt in enumerate(t, start=0):
        positionx, positiony = turt.pos()
        positiony = 0
        turt.pencolor("White")
        turt.goto(positionx, positiony)
        position[i] = positiony
        turt.pencolor(silks[i])
        turt.clear()
    global racing
    racing = False
    


def generate_turtles() -> None:
    for i in range(1, racing_turtles + 1):
        new_turtle = turtle.Turtle()
        new_turtle.pencolor(silks[i-1])
        new_turtle.pensize(3)
        t.append(new_turtle)
        position.append(0)

generate_turtles()

draw_finish_line()
draw_buttons()
starters_orders()


turtle.done()