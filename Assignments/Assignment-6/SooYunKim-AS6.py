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

def build_scale_matrix(x, y):
    m = identity_mat()
    m[0][2] = x
    m[1][2] = y
    return m

def build_trans_matrix(x, y):
    m = identity_mat()
    m[0][0] = x
    m[1][1] = y
    return m

def rotate_matrix(theta):
    m = identity_mat()
    m[0][0] = math.cos(theta)
    m[0][1] = -math.sin(theta)
    m[1][0] = math.sin(theta)
    m[1][1] = math.cos(theta)
    return m

def mat_pt_list(m, ptList):
    """ transform the entire ptList
    """
    return [mat_vec(m, v) for v in ptList]

""" Begin drawing
"""
print()
input("A: Show the basic plot, <CR> to continue")
w = 800
h = 600
td.create_plot(w, h, True)  # show the axis
ptList, sizeList, colorList = mf.getMyFace()
td.plot_points(ptList, sizeList, colorList)

print()
print("B: Translation Test: by (5, -2.5) in 30 steps")
for i in range(30):
    x = i * 5
    y = -i * 2.5
    print(f"                 by ({x}, {y})")
    scale_mat = build_scale_matrix(x, y)
    td.clear_plot(True) 
    newpts = mat_pt_list(scale_mat, ptList)
    td.plot_points(newpts, sizeList, colorList)

print()
input("<CR> to continue")
print("C: Scaling Test: by (0.01, -0.01) in 30 steps")
for i in range(30):
    x = 1 + i * 0.01
    y = 1 - 0.01 * i
    print(f"             by ({x:.4f}, {y:.4f})")
    scale_mat = build_trans_matrix(x, y)
    td.clear_plot(True) 
    newpts = mat_pt_list(scale_mat, ptList)
    td.plot_points(newpts, sizeList, colorList)

print()
input("<CR> to continue")
print("D: Rotation Test: by 2-degrees in 30 steps")
for i in range(0, 60, 2):
    print(f"              by {i}-degrees")
    theta = i * math.pi/180
    scale_mat = rotate_matrix(theta)
    td.clear_plot(True)  
    newpts = mat_pt_list(scale_mat, ptList)
    td.plot_points(newpts, sizeList, colorList)
