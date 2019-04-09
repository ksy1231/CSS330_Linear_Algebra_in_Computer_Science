from svg_draw import *
import math
from math import sin


width = 1200
height = 800  # define a 400x400 area, with (0,0) at the center
create_plot(width, height, True) # last parameter says draw axis/bound or not


"""
draw_point([0, 0],         20, "(255, 0, 0)")
draw_point([-width/2, 0],  10, "(0, 0, 255)")
draw_point([width/2, 0],   10, "(0, 255, 255)")
draw_point([0, height/2],  10, "(0, 255, 0)")
draw_point([0, -height/2], 10, "(0, 0, 0)")
draw_point([100, 100],      5, "(188, 244, 199)")
"""

eye_color = "(0, 0, 0)"
nose_color = "(0, 0, 200)"
mouth_color = "(255, 200, 200)"
L = [
    # Eyes
     [[-80, 120], 20, eye_color]  # left
    ,[[ 80, 120], 20, eye_color]  # right
    # Nose
   # ,[[0, 75], 10, nose_color]  # top dot
   # ,[[0, 65], 10, nose_color]  # 
    ,[[0, 55], 10, nose_color]  # 
    ,[[0, 45], 10, nose_color]  #
    ,[[0, 35], 10, nose_color]  #
    ,[[-6, 30], 10, nose_color]  # bottom two holes
    ,[[6, 30], 10, nose_color]  #
    # Mouth
    ,[[-70, -25], 10, mouth_color]  # left-top dot
    #,[[-65, -35], 10, mouth_color]  #
    ,[[-55, -45], 10, mouth_color]  #
    #,[[-45, -48], 10, mouth_color]  #
    ,[[-35, -52], 10, mouth_color]  #
    #,[[-25, -55], 10, mouth_color]  #
    ,[[-15, -55], 10, mouth_color]  #
    #,[[ -5, -55], 10, mouth_color]  #
    ,[[  0, -55], 10, mouth_color]  #  center
    ,[[ 70, -25], 10, mouth_color]  # 
    #,[[ 65, -35], 10, mouth_color]  #
    ,[[ 55, -45], 10, mouth_color]  #
    #,[[ 45, -48], 10, mouth_color]  #
    ,[[ 35, -52], 10, mouth_color]  #
    #,[[ 25, -55], 10, mouth_color]  #
    ,[[ 15, -55], 10, mouth_color]  #
    #,[[  5, -55], 10, mouth_color]  #
    ]

plot_points(L)

input("Type to when ready")

def scale_PosInfo(p, alpha):
    """
    Remember, PosInfo = [[x, y], size, "color"]
    scales: the point by alpha
    scales: the size by alpha
    """
    r = list()
    r.append([i*alpha for i in p[0]])
    r.append(p[1] * alpha)
    r.append(p[2])
    return r

def translate_PosInfo(p, delta):
    """ delta is [dx, dy]
    Remember, PosInfo = [[x, y], size, "color"]
    translates the point by delta 
    leave the rest untouched
    """
    r = list()
    r.append([p[0][0] + delta[0], p[0][1] + delta[1]])
    r.append(p[1])
    r.append(p[2])
    return r


def scale_PosInfoList(l, alpha):
    return [scale_PosInfo(i, alpha) for i in l]

def translate_PosInfoList(l, delta):
    return [translate_PosInfo(i, delta) for i in l]

def translate_and_plot(l, delta, showBounds = False):
    a = translate_PosInfoList(l, delta)
    clear_plot(showBounds)
    plot_points(a)


def scale_and_plot(l, alpha, showBounds = False):
    a = scale_PosInfoList(l, alpha)
    clear_plot(showBounds)
    plot_points(a)


a = scale_PosInfoList(L, 1)
scale = 30
for s in range(1, scale, 1):
    scale_and_plot(L, s/scale, True)

# move right-up
for d in range(0, 300, 20):
    translate_and_plot(L, [d, d], True)

a = translate_PosInfoList(L, [300, 300])
for d in range(0, -600, -20):
    translate_and_plot(a, [d, 0], True)

a = translate_PosInfoList(L, [-300, 300])
for d in range(0, 300, 20):
    translate_and_plot(a, [d, -d], True)
    
for s in range(scale, scale//5, -1):
    scale_and_plot(L, s/scale, True)
    

# Do the sine function
def mySine(x):
    return height/2 * sin(x * 2 * math.pi / (width / 4))

a = scale_PosInfoList(L, 0.3)
for r in range(6):
    for x in range(-600, 600, 10):
        delta = [x, mySine(x)]
        translate_and_plot(a, delta, True)
    for x in range(600, -600, -10):
        delta = [x, mySine(x)]
        translate_and_plot(a, delta, True)
        

close_plot()

