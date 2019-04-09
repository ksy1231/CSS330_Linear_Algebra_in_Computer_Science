#
# Empty Template
# Attempt at Class Exercise 10/19
#

from svg_draw import *
import math  # for math.sin() and math.pi functions

width = 600
height = 600

create_plot(width, height, True)

##L = [
##     [0, 0],       30, "(0, 0, 0)"
##     [-200, 0],    10, "(255, 0, 0)"
##     [200, 0],     10, "(0, 255, 0)"
##     [0, 200],     10, "(0, 0, 255)"
##     [0, -200],     10, "(0, 255, 255)"
##     [100, 100],   5, "(255, 128, 0)"
##     [100,-100],   5, "(50, 205, 50)"
##     [-100,-100],  5, "(51, 161, 201)"
##     [-100, 100],  5, "(255, 100, 255)"
##]
##
##plot_points(L)

#draw_point([10, 10], 30, "(255, 0, 0)") # [position], size, "color"

#clear_plot() # 
##draw_point([10, 10], 30, "(255, 0, 0)")
##
##clear_plot(True) # Notice the parameter: "True"
##draw_point([10, 10], 30, "(255, 0, 0)")

#draw_point([10, 10], 30, "(255, 0, 0)")

##for i in range(0, 200, 10):
##    draw_point([i, 0], 20, "(0, 255, 0)")

##for i in range(200, 0, -10):
##    clear_plot() # try without and with out the "True" parameter
##    draw_point([i, 0], 20, "(0, 0, 255)") # blue
##    draw_point([0, i], 20, "(0, 255, 255)") # aqua
##    draw_point([-i, 0], 20, "(0, 255, 0)") # green
##    draw_point([0, -i], 20, "(255, 0, 0)") # red

a = [0, 0]
b = [200, 0]
c = [0, 200]
d = [-200, 0]
e = [0, -200]
f = [100, 100]
g = [-100, 100]
h = [-100, -100]
k = [100, -100]

def create_points():
    draw_point(a, 30, "(0, 0, 0)") # black

    draw_point(b, 15, "(255, 0, 0)") # red
    draw_point(c, 15, "(0, 255, 0)") # green
    draw_point(d, 15, "(0, 0, 255)") # blue
    draw_point(e, 15, "(0, 255, 255)") # aqua

    draw_point(f, 8, "(255, 128, 0)") # orange
    draw_point(g, 8, "(50, 205, 50)") # limegreen
    draw_point(h, 8, "(51, 161, 201)") # peacock
    draw_point(k, 8, "(255, 100, 255)") # pink

def scalar_vector_mult(alpha, v): return [alpha*x for x in v]

def move_points():
    for i in range(10, 0, -1):
        j = i / 10
        print(i)
        print(scalar_vector_mult(i, b))
        #draw_point([scalar_vector_mult(i, b)], 15, "(255, 0, 0)")

move_points()
#draw_point([scalar_vector_mult(i/10, b) for i in range(11)], 5, "(255, 0, 0)")
#create_points()

