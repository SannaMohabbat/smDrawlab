from datetime import datetime
import turtle
import sys
import os
"""
this function prints the information
that was originally in the print
me first function onto the screen
created
"""
def print_info():
    s_x = 400
    s_y = -300
    x = s_x
    y = s_y
    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    name = "CNET-142 Sanna Mohabbat"
    turtle.write(name, align = "right",\
                 font=("Helvetica",10))

    y = y-(25)

    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    lab = "Lab 7 - Olympic Rings"
    turtle.write(lab,  align = "right",\
                 font=("Helvetica",10))

    y = y-(25)

    currentTime = datetime.now()
    timestampStr = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
        
    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(timestampStr,  align = "right",\
                 font=("Helvetica",10))



    
##    name = "CNET-142 Sanna Mohabbat"
##    # creating string called name, setting my name to it
##    print("{:14}".format("Name"),":", name)
##    # printing out string name
##    lab = "Lab 7 - Olympic Rings"
##    #creating string called lab, setting it equal to lab number and name
##    print("{:14}".format("Lab:"),":", lab)
##    #printing out lab
##    currentTime = datetime.now()
##    #setting currentTime to datetime and using datetime to find the date/time
##    timestampStr = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
##    #converting currentTime to a string
##    print("{:14}".format("Current Time"),":", timestampStr)
##    #printing out the time
