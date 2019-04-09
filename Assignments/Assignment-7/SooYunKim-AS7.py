# Author: Soo Yun Kim
# Assignment 7: Nov 16, 2018
# Date: Nov 16, 2018
    
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

def mat_pt_list(m, ptList):
    """ transform the entire ptList
    """
    return [mat_vec(m, v) for v in ptList]

"""
    Begin testing ...
"""

width = 800
height = 600
td.create_plot(width, height, True)
pts, sizes, colors = getMyFace()
td.plot_points(pts, sizes, colors)
input("A: Show the basic plot, <CR> to continue")

input("\nB: Mat_Mat Test: Scale first then rotate in 30 steps")
for i in range(0, 60, 2):
    td.clear_plot(True)
    r = rotate_mat(i)
    sx = 1 + i/2 * 0.01
    sy = 1 - 0.01 * i/2
    s = scale_mat(sx, sy)
    print(f"          scale: ({sx:3.2f}, {sy:3.2f})  then  rotate:{i:2}")
    cm = mat_mat(r, s)
    td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)

input("\n<CR> to continue")
print("C: Mat_Mat Test: Rotate first then Scale in 30 steps")
for i in range(0, 60, 2):
    td.clear_plot(True)
    r = rotate_mat(i)
    sx = 1 + i/2 * 0.01
    sy = 1 - 0.01 * i/2
    s = scale_mat(sx, sy)
    print(f"          rotate:{i:2}  then  scale: ({sx:3.2f}, {sy:3.2f})")
    cm = mat_mat(s, r)
    td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)

input("\n<CR> to continue")
print("D: Mat_Mat Test: Rotate first then Translation in 30 steps")
for i in range(0, 60, 2):
    td.clear_plot(True)
    r = rotate_mat(i)
    tx = int(i/2 * 5)
    ty = i
    t = trans_mat(tx, ty)
    print(f"          rotate:{i:2}  then  translate: ({tx}, {ty})")
    cm = mat_mat(t, r)
    td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)

input("\n<CR> to continue")
print("E: Mat_Mat Test: Translation first then Rotate in 30 steps")
for i in range(0, 60, 2):
    td.clear_plot(True)
    r = rotate_mat(i)
    tx = int(i/2 * 5)
    ty = i
    t = trans_mat(tx, ty)
    print(f"          translate: ({tx}, {ty})  then  rotate:{i:2}")
    cm = mat_mat(r, t)
    td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)

input("\n<CR> to continue")
print("F: At (150, 100) : Making a funny face")

def funny_face(x, y):
    for r in range(0, -45, -5):
        td.clear_plot(True)
        rm = rotate_mat(r)
        t = trans_mat(x, y)
        cm = mat_mat(t, rm)
        td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)
        
    for r in range(-45, 45, 5):
        td.clear_plot(True)
        rm = rotate_mat(r)
        t = trans_mat(x, y)
        cm = mat_mat(t, rm)
        td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)
        
    for s in range(1, 11):
        td.clear_plot(True)
        scale = 1 + s/20
        sm = scale_mat(scale, scale)
        t = trans_mat(x, y)
        cm = mat_mat(t, sm)
        td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)
        
    for s in range(1, 11):
        td.clear_plot(True)
        scale = 1.5 - s / 10
        sm = scale_mat(scale, scale)
        t = trans_mat(x, y)
        cm = mat_mat(t, sm)
        td.plot_points(mat_pt_list(cm, myface_pt_list()), sizes, colors)

funny_face(150, 100)

input("\n<CR> to continue")
print("G: Making funning face at Left Mouse Click")

td.turtle_draw_mouse_click(funny_face, 1)
