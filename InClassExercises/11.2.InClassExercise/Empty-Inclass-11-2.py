#
#
import sys
sys.path.append('./Lib')  # this is where all the library files are

import math
import turtle_draw as td
import MyFace as mf

""" Matrix Utilities
"""
def dot_vector(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

""" Begin drawing
"""
print()
print("Simple face plot with axis")
w = 800
h = 600
td.create_plot(w, h, True)  # show the axis
ptList, sizeList, colorList = mf.getMyFace()
td.plot_points(ptList, sizeList, colorList)

def f(x, y):
    print("Left Mouse click: x, y)")

    
td.turtle_draw_mouse_click(f, 1)
