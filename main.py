import turtle
import Draw_USA_Flag
import print_me_first

#create screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("white")
# set tile of screen
screen.bgpic("usa.png")
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


# we need to draw total 13 stripes, 7 red and 6 white
# so we first create, 6 red and 6 white stripes alternatively
for stripe in range(0,6):
    for color in ["red", "white"]:
        Draw_USA_Flag.draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
        # decrease value of y by stripe_height
        y = y - stripe_height

# create last red stripe
Draw_USA_Flag.draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
y = y - stripe_height


square_height = (7/13) * flag_height
square_width = (0.76) * flag_height
Draw_USA_Flag.draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')

gap_between_stars = 30
gap_between_lines = stripe_height + 6
y = 112
# create 5 rows of stars
for row in range(0,5) :
    x = -222
    # create 6 stars in each row
    for star in range (0,6) :
        Draw_USA_Flag.draw_star(x, y, 'white', star_size)
        x = x + gap_between_stars
    y = y - gap_between_lines

gap_between_stars = 30
gap_between_lines = stripe_height + 6
y = 100
# create 4 rows of stars
for row in range(0,4) :
    x = -206
    # create 5 stars in each row
    for star in range (0,5) :
        Draw_USA_Flag.draw_star(x, y, 'white', star_size)
        x = x + gap_between_stars
    y = y - gap_between_lines

Draw_USA_Flag.draw_ring()
Draw_USA_Flag.draw_name()

print_me_first.print_info()

screen.mainloop()




