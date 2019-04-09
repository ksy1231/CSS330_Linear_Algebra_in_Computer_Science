from svg_draw import *
import math  # for math.sin() and math.pi functions

width = 600
height = 600

right = 200
left = -200
up = 200
down = -200

L = [
    [ [0, 0],       30],
    [ [right, 0],   10],
    [ [0, up],      10],
    [ [left, 0],    10],
    [ [0, down],    10],
    [ [100, 100],    5],
    [ [-100, 100],   5],
    [ [-100, -100],  5],
    [ [100, -100],   5]
    ]

def draw_the_points(L):
    draw_point(L[0][0], L[0][1], "(0, 0, 0)") # black

    draw_point(L[1][0], L[1][1], "(255, 0, 0)") # red
    draw_point(L[2][0], L[2][1], "(0, 255, 0)") # green
    draw_point(L[3][0], L[3][1], "(0, 0, 255)") # blue
    draw_point(L[4][0], L[4][1], "(0, 255, 255)") # aqua

    draw_point(L[5][0], L[5][1], "(255, 128, 0)") # orange
    draw_point(L[6][0], L[6][1], "(50, 205, 50)") # limegreen
    draw_point(L[7][0], L[7][1], "(51, 161, 201)") # peacock
    draw_point(L[8][0], L[8][1], "(255, 100, 255)") # pink

# Problem 1
print("\n\n")
print("Problem 1: drawing at 9 positions with different sizes and colors")
create_plot(width, height, True)
draw_the_points(L)

# Problem 2
input("type return for problem 2 output")
print("\n\n")
print("Problem 2: same positions without axis or boarders")
clear_plot()
draw_the_points(L)

def scale_pt(p, alpha):
    return [p[0]*alpha, p[1]*alpha]

def scale_pt_list(l, alpha):
    return [[scale_pt(i[0], alpha), i[1]*alpha] for i in l]

# Problem 3
input("type return for problem 3 output")
print("\n\n")
print("Problem 3: 10-frame animation from simple scaling function")
for i in range(10, 1, -1):
    b = scale_pt_list(L, i /10)
    clear_plot()
    draw_the_points(b)

def translate_pt(p, delta):
    return [p[0]+delta[0], p[1]+delta[1]]

def translate_pt_list(l, delta):
    return [[translate_pt(i[0], delta), i[1]] for i in l]

# Problem 4
input("type return for problem 4 output")
print("\n\n")
print("Problem 4: 10-frame animation from simple translation function")
a = scale_pt_list(L, 0.2)
for i in range(0, 300, 10):
    b = translate_pt_list(a, [i, i])
    clear_plot()
    draw_the_points(b)
