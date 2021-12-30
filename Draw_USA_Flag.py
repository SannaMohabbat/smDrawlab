import turtle
import os
import sys

#create screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("white")
# set tile of screen

screen.title("USA Flag - https://www.pythoncircle.com")
# "Yesterday is history, tomorrow is a mystery, 
# but today is a gift. That is why it is called the present.”
# — Oogway to Po, under the peach tree, Kung Fu Panda Movie
oogway = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
oogway.speed(1000)
oogway.penup()
# decide the shape of cursor/turtle
oogway.shape("turtle")

# flag height to width ratio is 1:1.9
flag_height = 250
flag_width = 475

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -237
start_y = 125


# For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
stripe_height = flag_height/13
stripe_width = flag_width

# length of one arm of star
star_size = 10

x = start_x
y = start_y
"""
this function is to fill in the rectangle for the
flag and takes in five params
x and y - the points needed to be moved
height - height of rect
width - width of rect
color - color of rect
"""
def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()
"""
this function is to draw and create
points of where the stars are on the
USA flag and takes in four params
x and y - points of each star
color- color of star
length- length of star
"""
def draw_star(x,y,color,length) :
    oogway.goto(x,y)
    oogway.setheading(0)
    oogway.pendown()
    oogway.begin_fill()
    oogway.color(color)
    for turn in range(0,5) :
        oogway.forward(length)
        oogway.right(144)
        oogway.forward(length)
        oogway.right(144)
    oogway.end_fill()
    oogway.penup()
"""
this function is to draw the rings
for the olympic rings
takes no params
"""
def draw_ring():
        # Named constants
    RADIUS = 70
    STARTING_POINT_X = -200
    STARTING_POINT_Y = -300


    x = STARTING_POINT_X
    y = STARTING_POINT_Y

    color = "blue"  #ADD IN MAIN
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle


    x = STARTING_POINT_X + 100
    y = STARTING_POINT_Y - 50

    color = "orange"  #ADD IN MAIN
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle

    x = STARTING_POINT_X + 200
    y = STARTING_POINT_Y + 10


    color = "black"  #ADD IN MAIN
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle

    x = STARTING_POINT_X + 300
    y = STARTING_POINT_Y - 50

    color = "green"  #ADD IN MAIN
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle

    x = STARTING_POINT_X + 400
    y = STARTING_POINT_Y + 10

    color = "red"  #ADD IN MAIN
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup() # when penup is set, drawing is disabled when move the cursor
    turtle.goto(x, y) # move the cursor to (x, y)
    turtle.pendown() #when pendown is setup, drawing is enabled
    turtle.circle(RADIUS) # draw a circle
"""
this function draws the name on the top of
the screen
takes no params
"""
def draw_name():
    STRT_X = 10
    STRT_Y = 120
    x = STRT_X
    y = STRT_Y
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor('blue')
    turtle.write("USA OLYMPIC TEAM", align="center",\
                 font =("Helvetica", 60,"bold"))

    
