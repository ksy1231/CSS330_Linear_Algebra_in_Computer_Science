# Author: Kelvin Sung
# Assignment 7: Solution
# Date: Nov 9, 2018
    
# Import the necessary libraries

import sys
sys.path.append('./Lib')  # this is where all the library files are

import math
import turtle_draw as td
from MyFace import *

""" Matrix utilities
"""

def dot_vector(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))


def identity_mat():
    """
    returns the identity matrix in R-3
    """
    return [ [1 if i == j else 0 for i in range(3)] for j in range(3) ]


def mat_vec(m, v):   # matrix is 3x3 vectors are 2
    """
    Multiplies the matrix to the vector
         m[0][2] is added to x (translation)
         m[1][2] is added to y
    """
    return [dot_vector(m[0], v)+m[0][2], dot_vector(m[1], v) + m[1][2]]


def col_vec(m, i):  # create column vectors, i is 0, 1, or 2
    return [m[0][i], m[1][i], m[2][i]]

def mat_mat_v0(m1, m2):  #
    """
    two 3x3 matrices,
    matrix-matrix multiplication, returns a new matrix
    """
    return [ [dot_vector(m1[0], col_vec(m2, 0)), dot_vector(m1[0], col_vec(m2, 1)), dot_vector(m1[0], col_vec(m2, 2))],
             [dot_vector(m1[1], col_vec(m2, 0)), dot_vector(m1[1], col_vec(m2, 1)), dot_vector(m1[1], col_vec(m2, 2))],
             [dot_vector(m1[2], col_vec(m2, 0)), dot_vector(m1[2], col_vec(m2, 1)), dot_vector(m1[2], col_vec(m2, 2))]
            ]

def mat_mat(m1, m2):  # two 3x3 matrices, with comprehension
    return [ [dot_vector(m1[i], col_vec(m2, j)) for j in range(3)]
                 for i in range(3) ]


def trans_mat(x, y):
    """
    Constructs and returns a translation matrix
    """
    m = identity_mat()
    m[0][2] = x
    m[1][2] = y
    return m


def scale_mat(x, y):
    """
    Constructs and returns a scaling matrix
    """
    m = identity_mat()
    m[0][0] = x
    m[1][1] = y
    return m


def rotate_mat(theta):
    """
    theta: is an angle in degree
    Constructs and returns a rotation matrix
    """
    m = identity_mat()
    theta = math.radians(theta)
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    m[0][0] =  cosTheta
    m[0][1] = -sinTheta
    m[1][0] =  sinTheta
    m[1][1] =  cosTheta
    return m


""" Testing the utilities
"""


width = 800
height = 600
td.create_plot(width, height, True)

def xform_pt_list(m, ptlist):
    """ Transform a list of points
        ptlist: [  [x, y],  [x, y] ... ]
    """
    return [mat_vec(m, v) for v in ptlist]

    
# test translate matrix
steps = 30
sx = 0.01
sy = -0.01
deg = 2


# matrice geneation functions
def scale_test(d):
    ux = 1+d*sx
    uy = 1+d*sy
    sm = scale_mat(ux, uy)
    msg = f'scale:({ux:1.2f}, {uy:1.2f})'
    return sm, msg

def rotate_test(d):
    ud = d * deg
    rm = rotate_mat(ud)
    msg = f'rotate:{ud:2.0f}'
    return rm, msg

def trans_test(d):
    tx = d * 5
    ty = d * 2
    tm = trans_mat(tx, ty)
    msg = f'translate({tx:1.0f}, {ty:1.0f})'
    return tm, msg


pts, sizes, colors = getMyFace()
td.plot_points(pts, sizes, colors)
input("A: Show the basic plot, <CR> to continue")

print()
print(f"B: Mat-Mat Test: Rotate followed by Scale in {steps} steps")
for d in range(steps):
    td.clear_plot(True)
    sm, smsg = scale_test(d)
    rm, rmsg = rotate_test(d)
    cm = mat_mat(rm, sm)
    print("         ", smsg, " then ", rmsg)
    td.plot_points(xform_pt_list(cm, myface_pt_list()), sizes, colors)
input("\n<CR> to continue")


print(f"C: Mat-Mat Test: Scale followed by Rotate in {steps} steps")
for d in range(steps):
    td.clear_plot(True)
    sm, smsg = scale_test(d)
    rm, rmsg = rotate_test(d)
    cm = mat_mat(sm, rm)
    print("         ", rmsg, " then ", smsg)
    td.plot_points(xform_pt_list(cm, myface_pt_list()), sizes, colors)
input("\n<CR> to continue")


print(f"D: Mat-Mat Test: rotate followed by Translation in {steps} steps")
for d in range(steps):
    td.clear_plot(True)
    tm, tmsg = trans_test(d)
    rm, rmsg = rotate_test(d)
    cm = mat_mat_v0(tm, rm)
    print("         ", rmsg, " then ", tmsg)
    td.plot_points(xform_pt_list(cm, myface_pt_list()), sizes, colors)
input("\n<CR> to continue")


print(f"E: Mat-Mat Test: Translation followed by scaling in {steps} steps")
for d in range(steps):
    td.clear_plot(True)
    tm, tmsg = trans_test(d)
    rm, rmsg = rotate_test(d)
    cm = mat_mat_v0(rm, tm)
    print("         ", tmsg, " then ", rmsg)
    td.plot_points(xform_pt_list(cm, myface_pt_list()), sizes, colors)
input("\n<CR> to continue")


def draw_pts(p):
    td.clear_plot(True)
    td.plot_points(p, sizes, colors)


def wave(start, end, step, tm):
    for r in range(start, end, step):
        rm = rotate_mat(r)
        tr = mat_mat(tm, rm)
        a = xform_pt_list(tr, pts)
        draw_pts(a)

def shrink(start, end, fs, tm):
    for s in range(start, end):
        scale = fs(s)
        sm = scale_mat(scale, scale)
        ts = mat_mat(tm, sm)
        a = xform_pt_list(ts, pts)
        draw_pts(a)
   
def myFunc(x, y):
    tm = trans_mat(x, y)
    a = xform_pt_list(tm, pts)
    td.clear_plot()
    draw_pts(a)
    wave(0, -45, -5, tm)
    wave(-45, 45, 5, tm)
    shrink(1, 11, lambda s: 1 + s/20,    tm)
    shrink(1, 11, lambda s: 1.5 - s /10, tm)


print("F: At (150, 100): Making a funny face")
myFunc(150, 100)
input("<CR> to continue")

print()
print("G: Making funning face at Left Mouse Click")
td.turtle_draw_mouse_click(myFunc, 1)
