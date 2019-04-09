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
#print("Simple face plot with axis")
##w = 800
##h = 600
##td.create_plot(w, h, True)  # show the axis
##ptList, sizeList, colorList = mf.getMyFace()
##td.plot_points(ptList, sizeList, colorList)

def f(x, y):
    print(f"Left Mouse click: {x}, {y})")
    T = make_a_translation_matrix(x, y)
    new_pt_list = mat_vec_multiply(T, ptList)
    td.plot_points(new_pt_list, sizeList, colorList)
    
#td.turtle_draw_mouse_click(f, 1)

def mat_vec(m, v):
    return [ dot_vector(m[r], v) + m[r][len(m)-1] for r in range(len(m)-1) ]

def mat_vec_list(m, lst):
    return [mat_vec(m, i) for i in lst]
    
print("A: Printing the 3x3 Indentify Matrix")
input("<CR> to continue")
I3 = [ [1, 0, 0],
       [0, 1, 0],
       [0, 0, 1] ]
print(f"I3 = {I3}")

print()
print("B: Testing matrix-vector multiplication with I3")
input("<CR> to continue")
v1 = [1, 2]
print(f"v1 = {v1}")
print(f"I3 * v1 = {mat_vec(I3, v1)}")
v2 = [3, 4]
print(f"v2 = {v2}")
print(f"I3 * v2 = {mat_vec(I3, v2)}")

print()
print("C: Testing matrix-vector multiplication with an arbitrary matrix")
input("<CR> to continue")
m = [ [1, 2, 3],
      [3, 4, 5],
      [6, 7, 8] ]
print(f"m = {m}")
print(f"v1 = {v1}")
print(f"m * v1 = {mat_vec(m, v1)}")
print(f"v2 = {v2}")
print(f"m * v2 = {mat_vec(m, v2)}")

print()
print("D: Testing matrix-vector multiplication with a list of 2-vectors")
input("<CR> to continue")
l = [[1, 2], [3, 4], [5, 6]]
print(f"Given a list of points: {l}")
print(f"Results of multiplying the list by m is: {mat_vec_list(m, l)}")
