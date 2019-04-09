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


def trans_mat(x, y):
    """
    constructs a translation by (x, y) matrix
    """
    m = identity_mat()
    m[0][2] = x
    m[1][2] = y
    return m

def mat_pt_list(m, ptList):
    """ transform the entire ptList
    """
    return [mat_vec(m, v) for v in ptList]


"""
    Begin testing ...
"""

print("A: Printing the 3x3 Indentiy Matrix")
input("<CR> to continue")
I3 = identity_mat()
print("I3 = ", I3)
print()

print("B: Testing matrix-vector multiplication with I3")
input("<CR> to continue")
v1 = [1, 2]
v2 = [3, 4]
print("v1 = ", v1)
print("I3 * v1 = ", mat_vec(I3, v1))
print("v2 = ", v2)
print("I3 * v2 = ", mat_vec(I3, v2))

print()
print("C: Testing matrix-vector multiplication with an arbitrary matrix")
input("<CR> to continue")
m = [ [1, 2, 3], [3, 4, 5], [6, 7, 8]]
print("m = ", m)
print("v1 = ", v1)
print("m * v1 = ", mat_vec(m, v1))
print("v2 = ", v2)
print("m * v2 = ", mat_vec(m, v2))

""" Begin drawing
"""
print()
print("D: Simple face plot with axis")
input("<CR> to continue")
w = 800
h = 600
td.create_plot(w, h, True)  # show the axis
ptList, sizeList, colorList = mf.getMyFace()
td.plot_points(ptList, sizeList, colorList)

print()
print("E: Testing mouse clicks")

def mmb(x, y):
    print(f'Middle mouse click at: {x:4.2f} and {y:4.2f}')

td.turtle_draw_mouse_click(mmb, 2)

print()
print("F: Click and draw")
def draw_at(x, y):
    print(f'Left mouse click at: {x:4.2f} and {y:4.2f}')
    td.clear_plot()
    t = trans_mat(x, y)
    newpts = mat_pt_list(t, ptList)
    td.plot_points(newpts, sizeList, colorList)

    
td.turtle_draw_mouse_click(draw_at, 1)
