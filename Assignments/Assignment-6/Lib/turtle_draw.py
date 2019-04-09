# Original Copyright 2013 Philip N. Klein
#
"""
This file contains a simple plotting interface based on the default
Python turtle graphics. The main functionality achieved is hidding the
"current position" of turtle graphics. 

Generate the documentation file by:

    python -m pydoc -w turtle_draw

Author: Kelvn Sung
Date: Oct 2018
"""
import turtle
from turtle import Turtle
import time as tm
      
_t = Turtle()

# Not eligant but works
def create_plot(w, h, drawBounds = False):  
    """
    Creates a w by h drawing area based on the default turtle drawing lib

    :param drawBounds: when true the x/y axis and plot bounds will be drawn
        
    """
    global _llx, _lly, _urx, _ury
    _llx = -w/2
    _lly = -h/2
    _urx = w/2
    _ury = h/2
    turtle.mode('world')
    turtle.setup(w, h)
    turtle.colormode(255)
    turtle.tracer(0, 0)
    turtle.screensize(w, h)
    turtle.setworldcoordinates(_llx, _lly, _urx, _ury)
    _t.reset()
    _t.hideturtle()
    clear_plot(drawBounds)
    
    
def close_plot():
    """
    Closes the current drawing session. After this none
    of the drawing command will work.
    """
    _t.bye()


def clear_plot(drawBounds = False):
    """ Clears everything 
        :param drawBounds: when true the x/y axis and plot bounds will be drawn
    """
    # turtle.delay(100)
    tm.sleep(0.03)  # for some reasons, I can't get delay() to work, so time
    _t.clear()
    _t.penup()
    if (drawBounds):
        draw_axis()
        draw_bounds()
    

def draw_axis():
    """ Draws the X/Y axis
    """
    draw_line([_llx,  0], [_urx,   0], (0, 0, 0), 2)  # X-axis line
    draw_line([0, _lly], [0, _ury],   (0, 0, 0), 2)  # Y-axis line
    show_plot()

def draw_bounds():
    """ Draws the four surrounding bounds
    """
    bc = (200, 200, 200) # bound color
    bw = 1 #bound width
    draw_line([_llx,  _ury], [_urx, _ury], bc, bw)  # Top
    draw_line([_llx,  _lly], [_urx, _lly], bc, bw)  # bottom
    draw_line([_llx,  _lly], [_llx, _ury], bc, bw)  # left
    draw_line([_urx,  _lly], [_urx, _ury], bc, bw)  # right
    show_plot()

def draw_line(p1, p2, color, width):
    """ Draws a line in "color" with "width" from p1 to p2
    """
    _t.setx(p1[0])
    _t.sety(p1[1])
    _t.pendown()
    _t.pensize(width)
    _t.pencolor(color)
    _t.goto(p2[0], p2[1])
    _t.penup()
    _t.hideturtle()
    
    

def draw_point(p, size, color):
    """ Draws a point, with size, and color at p
    """
    draw_circle(p, size, color)
    

def draw_circle(center, radius, color):
    """ Draws a circle with radius and radius at center
    """
    _t.penup()
    _t.goto(center[0], center[1]-radius)
    _t.pendown()
    _t.pencolor(color)
    _t.fillcolor(color)
    _t.begin_fill()
    _t.circle(radius)
    _t.end_fill()
    _t.penup()
    _t.hideturtle()
    
    
def show_plot():
    """
    call this at the end of your drawing and when you want to see everything
    """
    turtle.update()
    

def plot_points(pt_list, size_list, color_list):
    """
       Input three lists must be the same length
       input format,
           pt_list =    [ [x1, y1], [x2, y2] ... ]
           size_list =  [ size1,    size2,   ... ]
           color_list = [ color1,   color2,  ... ]
turtle_draw.pyx1, y1], etc.
    """
    for i in range(len(pt_list)):
        draw_circle(pt_list[i], size_list[i], color_list[i])
    show_plot()


def _w2p(p):
    return [_cx+p[0], _cy-p[1]]


def _color_str(tup):
    """ tup: in the format of (r, g, b): three 0 to 255 integers
    output: '#RRGGBB' in hex string suitable for turtle graphics
    """
    a = ''
    for i in tup:
        a = a + hex(i)[2:]
    return '#' + a

#"""""""""""""""""""""""""""""
# For input support
def turtle_draw_mouse_click(f, n):
    """
    Sets up the call back function for when a mouse is clicked.
    
    f: is a function that accepts (x, y) parameters (mouse click position)
    n: is a number 1-Left Mouse, 2-Middle Mouse 3-Right Mouse
    
    f(x,y): will be called when user click the corresponding mouse button
    in the turtle drawing area.
    """
    turtle.Screen().onscreenclick(f, n)
