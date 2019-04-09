# Original Copyright 2013 Philip N. Klein
#
# Copied and modified by Kelvin Sung, Fall 2018
"""
This file contains a simple plotting interface, which uses a browser with SVG to
present a plot of points represented as either complex numbers or 2-vectors.

    ::Warning::
    
    This is a rather computing intensive HTML page.
    To support real-time animation-like behavior, the page activates
    the "reload()" function in javascript and attempts to reload
    the generated htmp file (Plot.html) at 80 ms interval!
    This design is not scalable for even moderate-size drawing operations.
    DO NOT darw too much stuff, and use with care. When the browser
    behaves "strangely" quit and re-start.
    Finally, make sure to close the webbrowser after you are done coding.

Tested on: Chrome (extensive), briefly: Edge, Firefox
  
Author: Kelvn Sung
Date: Oct 2018
Referenced: Philip Klein's plotting.py file from his book
"""
import webbrowser
import os
import time


_xoff = 40
_yoff = 40

# Not eligant but works
def create_plot(w, h, drawBounds = False):
    """
    Creates a w by h drawing area
    Using HTML SVG, open the html file using your default browser

    :param drawBounds: when true the x/y axis and plot bounds will be drawn
        
    """
    global _w
    global _h
    global _cx
    global _cy
    global _plot_file
    global _f
    _plot_file = 'Plot.html'
    _cx = _xoff + w/2
    _cy = _yoff + h/2
    _w = w
    _h = h
    _f = open(_plot_file, 'r+')
    clear_plot(drawBounds)
    file_to_open = 'file://' + os.getcwd() + '/' + _plot_file
    print('Displaying on your web-browser:', file_to_open)
    webbrowser.get(None).open(file_to_open)
    
def close_plot():
    """
    Closes the current drawing session. After this none
    of the drawing command will work.
    """
    _f.close()


def clear_plot(drawBounds = False):
    """ Clears everything from the HTML file
          Browser will show a empty page
        :param drawBounds: when true the x/y axis and plot bounds will be drawn
    """
    time.sleep(0.08) # wait a little to avoid causing too much resources
    _f.seek(0)
    _f.writelines(
        ['<!DOCTYPE html>\n'
        ,'<head>\n'
        ,'<title>plot</title>\n'
        ,'</head>\n'
        ,'<body>\n'])
    _f.writelines(
        ['<script type="text/javascript">\n'
         ' <!-- from: https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep --> \n'
         'function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms));}\n'        
         'requestAnimationFrame(async function () { await sleep(80); location.reload(); });\n'
         '</script>\n'])
    svg = '<svg height="%d" width="%d" xmlns="http://www.w3.org/2000/svg">\n' %(_h+(_yoff*2), _w+(_xoff*2))
    _f.writelines(svg)
    if (drawBounds):
        draw_axis()
        draw_bounds()
    _f.truncate()
    _f.flush();
    

def draw_axis():
    """ Draws the X/Y axis
    """
    draw_line([-_w/2,  0], [_w/2,   0], "(0, 0, 0)", 2)  # X-axis line
    draw_line([0, -_h/2], [0, _h/2],   "(0, 0, 0)", 2)  # Y-axis line

def draw_bounds():
    """ Draws the four surrounding bounds
    """
    bc = "(200, 200, 200)" # bound color
    bw = 1 #bound width
    draw_line([-_w/2,  _h/2], [_w/2, _h/2], "(100, 100, 100)", bw)  # Top
    draw_line([-_w/2,  -_h/2], [_w/2, -_h/2], "(100, 100, 100)", bw)  # bottom
    draw_line([-_w/2,  _h/2], [-_w/2, -_h/2], "(200, 100, 100)", bw)  # left
    draw_line([_w/2,  _h/2], [_w/2, -_h/2], "(100, 200, 100)", bw)  # right

def draw_line(p1, p2, color, width):
    """ Draws a line in "color" with "width" from p1 to p2
    """
    p1 = _w2p(p1)
    p2 = _w2p(p2)
    _f.writelines(['<line x1="%d" y1="%d" x2="%d" y2="%d"' % (p1[0], p1[1], p2[0], p2[1])
                   ,'style="stroke:rgb%s;stroke-width:%d"/>\n' %(color, width)])
    

def draw_point(p, size, color):
    """ Draws a point, with size, and color at p
    """
    draw_circle(p, size, color)
    

def draw_circle(center, radius, color):
    """ Draws a circle with radius and radius at center
    """
    center = _w2p(center)
    _f.writelines(['<circle cx="%d" cy="%d" r="%d" fill="rgb%s"/>\n'
                          % (center[0],center[1],radius, color)])
    show_plot()
    

def draw_rect(lower_left, width, height, color):
    p = _w2p(lower_left)
    p[1] = p[1]-height
    _f.writelines(['<rect x="%d" y="%d" width="%d" height="%d" fill="rgb%s"/>\n'
                          % (p[0],p[1],width, height, color)])
    

def show_plot():
    """
    call this at the end of your drawing and when you want to see everything
    """
    _f.flush()

def plot_points(L):
    """
       Plots input points
       input format,
            L = [ PosInfo, PosInfo ... ]
       where
           PosInfo = [ [x position, y position], size, "(r, g, b)" ]
    """
    for p in L:
        draw_circle(p[0], p[1], p[2])
    show_plot()


def _w2p(p):
    return [_cx+p[0], _cy-p[1]]
