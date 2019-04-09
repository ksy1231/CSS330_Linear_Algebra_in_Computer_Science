# Author: Kelvin Sung
# In-class Exercise: Nov 9, 2018
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

def col(m, i):
    return [m[0][i], m[1][i], m[2][i]]

def mat_mat(m1, m2):
    return [ [dot_vector(m1[r], col(m2, c)) for c in range(len(m1[r]))]
             for r in range(len(m1)) ]
                      
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

print("A: verify mat-mat function")
m1 = [ [1, 2, 3], [2, 3, 4], [5, 6, 7]]
m2 = [ [3, 4, 5], [1, 2, 3], [8, 9, 10]]
print("m1=", m1)
print("m2=", m2)
print("mat_mat(m1, m2):", mat_mat(m1, m2))

width = 800
height = 600
td.create_plot(width, height, True)

pts, sizes, colors = getMyFace()
input("\nB: Show the basic plot, <CR> to continue")
td.plot_points(pts, sizes, colors)

input("\nC: Transform by cm = T(200, -100) * R(45)")
td.clear_plot(True)
rm = rotate_mat(45)
tm = trans_mat(200, -100)
m = mat_mat(tm, rm)
td.plot_points(mat_pt_list(m, pts), sizes, colors)

input("\nD: Transform by cm = R(45) * T(200, -100)")
td.clear_plot(True)
m = mat_mat(rm, tm)
td.plot_points(mat_pt_list(m, pts), sizes, colors)
