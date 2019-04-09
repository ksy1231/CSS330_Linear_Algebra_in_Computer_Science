# Author: Kelvin Sung
# Assignment 6: Solution
# Date: Oct 18, 2018
    
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


def rotate_mat(theta, dummy):  # to support mat_test calling with 2 parameters
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


##
## V2: defines this function for testing all three of the matrices
##
def mat_test(steps, fx, fy, mat_func):
    for d in range(steps):
        td.clear_plot(True)
        dx = fx(d, delta)
        dy = fy(d, delta)
        print(f"           by ({dx:2.4f}, {dy:2.4f})")
        m = mat_func(dx, dy)
        td.plot_points(xform_pt_list(m, myface_pt_list()), sizes, colors)
    input("\n<CR> to continue")



pts, sizes, colors = getMyFace()
td.plot_points(pts, sizes, colors)
input("A: Show the basic plot, <CR> to continue")
# test translate matrix
steps = 30

print()
delta = 5
print(f"B: Translation Test: by ({delta}, {-delta/2}) in {steps} steps")
mat_test(steps,  # steps
         lambda d, delta: d*delta,      # compute dx
         lambda d, delta: d*(-delta/2), # compute dy
         trans_mat  # which matrix function to test
         )

    
sx = 0.01
sy = -0.01
print(f"C: Scaling Test: by ({sx:2.2f}, {sy:2.2f}) in {steps} steps")
mat_test(steps,  # steps
         lambda d, delta: 1+d*sx,  # compute dx
         lambda d, delta: 1+d*sy,  # compute dy
         scale_mat  # which matrix function to test
         )

deg = 2
print(f"D: Rotation Test: by {deg:2.0f}-degrees in {steps} steps")
mat_test(steps,  # steps
         lambda d, delta: d *deg,  # compute dx
         lambda d, delta: 0.0,    # does not have second parameter
         rotate_mat  # which matrix function to test
         )
