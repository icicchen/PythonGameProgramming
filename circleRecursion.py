import turtle
import colorsys
###################Library################
def drawcircle(x, y, radius, t):
    '''____________________________
    :param x: ____________________
    :param y:____________________
    :param radius:_______________
    :param t:____________________
    :return: _____________________
    '''
    moveturtle(x, y-radius)
    # pen color
    (r, g, b) = colorsys.hsv_to_rgb(float(radius) / 150, 1.0, 1.0)
    t.pencolor(r, g, b)
    # draw circle
    t.circle(radius)
    # return to the initial position
    moveturtle(x, y)
    # smaller circles
    if radius > 10:
        drawcircle(x+radius, y, radius/2, t)
        drawcircle(x-radius, y, radius/2, t)

def moveturtle(x, y):
    '''___________________________________
    :param x: __________________________
    :param y:__________________________
    :return: ___________________________
    '''
    t.up()
    t.setposition(x, y)
    t.down()
    #######################################


t = turtle.Turtle()
t.pensize(2)
moveturtle(-50, 0)
myWin = turtle.Screen()
drawcircle(x=1, y=100, radius=90,t=t)
myWin.exitonclick()


# ----------------------------------------------------------- #

import turtle
import colorsys
###################Library################
def drawcircle(x, y, radius, t):
    '''this function sets the pencolor and draws circles
    :param x: the x coordinate in which the turtle is located
    :param y: the y coordinate in which the turtle is located
    :param radius: sets the radius for the various sizes of circles
    :param t: turtle
    :return: None
    '''
    moveturtle(x, y-radius)
    # pen color
    (r, g, b) = colorsys.hsv_to_rgb(float(radius) / 150, 1.0, 1.0)
    t.pencolor(r, g, b)
    # draw circle
    t.circle(radius)
    # return to the initial position
    moveturtle(x, y)
    # smaller circles
    if radius > 10:
        drawcircle(x+radius, y, radius/2, t)
        drawcircle(x-radius, y, radius/2, t)

def moveturtle(x, y):
    '''this function moves the turtle while drawing the circles
    :param x: the x coordinate in which the turtle is located
    :param y: the y coordinate in which the turtle is located
    :return: None
    '''
    t.up()
    t.setposition(x, 1.8 * y)
    t.down()
    #######################################


t = turtle.Turtle()
t.pensize(2)
moveturtle(-50, 0)
myWin = turtle.Screen()
drawcircle(x=1, y=100, radius=90,t=t)
myWin.exitonclick()
