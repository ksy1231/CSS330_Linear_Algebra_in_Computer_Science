# Author: Soo Yun Kim
# Attempt at assignment 5 10/29
#
import math
from math import sin
import sys
sys.path.append('./Lib')  # this is where all the library files are
from image_mat_util import file2image
from image_mat_util import image2display
from image_mat_util import image2file  # in case you want to save to a file


image1 = file2image("SourceImages/s1-256.png")
image2 = file2image("SourceImages/s2-256.png")
#   image[row][column]
#   len(image) says how many rows [y-size, or height]
#   len(image[0]) says how many column [x-size, or width]
# image2display(m)

def scale_pixel(alpha, p):   # p is a tuple (R G B A)
    return tuple(alpha * i for i in p)

def add_pixel(p1, p2):
    return tuple(a+b for a, b in zip(p1,p2))

def convex_sum(s1, s2, alpha, beta):
    return [[add_pixel(scale_pixel(alpha, s1[r][c]), scale_pixel(beta, s2[r][c]))
             for c in range(len(s1[r]))]
            for r in range(len(s1)) ]

def scale_image(alpha, s2):
    return [ [scale_pixel(alpha, s2[r][c]) for c in range(len(s2[r])) ]
              for r in range(len(s2)) ]

def color_shift_image(delta, s2):   # assume same resolution!
    return [ [add_pixel(delta, s2[r][c]) for c in range(len(s2[r])) ]
              for r in range(len(s2)) ]

##input("<CR> to see A: Convex sum, from 0 to 1, in steps of 0.1")
##for i in range(0, 11, 1):
##    alpha = i/10
##    beta = 1-(i/10)
##    print("Cross blend alpha=", alpha, "beta=", beta)
##    image2display(convex_sum(image1, image2, alpha, beta))
##
##print("")
##input("<CR> to see B: Affine sum, from 1 to 2, in steps of 0.1")
##for i in range(0, 11, 1):
##    alpha = 1 + i/10
##    beta = -i/10
##    print("Cross blend alpha=", alpha, "beta=", beta)
##    image2display(convex_sum(image1, image2, alpha, beta))
##
##print("")
##input("<CR> to see C: Brighten image to 300% in 10 steps")
##for i in range(0, 21, 2):
##    alpha = 1 + i/10
##    print("scaling image by alpha=", alpha)
##    image2display(scale_image(alpha, image2))
##
##print("")
##input("<CR> to see D: increases image brightness by 250 by 25 in each step")
##for i in range(25, 251, 25):
##    delta = (i,)*3
##    print("Shift by delta=", delta)
##    image2display(color_shift_image(delta, image2))
##
##print("")
##input("<CR> to see E: remove R-Channel by 25 in e ach step")
##for i in range(0, -251, -25):
##    delta = (i, 0, 0)
##    print("Shift R-Channel delta=", delta)
##    image2display(color_shift_image(delta, image2))
##    a = color_shift_image(delta, image2)
##
##print("")
##input("<CR> to see F: continue to remove image G-Channel by 25 in each step")
##for i in range(0, -251, -25):
##    delta = (0, i, 0)
##    print("Shift R-Channel delta=", delta)
##    image2display(color_shift_image(delta, a))

##print("")
##input("<CR> to see G: Darken image to 50% in 11 steps")
##for i in range(100, 49, -5):
##    alpha = i/100
##    print("Scaling image by alpha=", alpha)
##    image2display(scale_image(alpha, image2))
##
##print("")
##input("<CR> to see H: Modulate R-Channel by 2 periods of amplitude 100 sine function:")
##
ImageWidth = 256
N = 2
amp = 100

def sine(x):
    return amp * sin(x * N * 2 * math.pi / ImageWidth)

def show_sine(s2):
    return [ [add_pixel(s2[r][c], [sine(c), 0, 0]) for c in range(len(s2[r])) ]
              for r in range(len(s2)) ]
##             
##image2display(show_sine(image2))

print("")
input("<CR> to see I: Sine function phase shift by PI (180-degree) in 20 steps:")

def show_shift_sine(s2, i):
    return [ [add_pixel(s2[r][c], [sine(c - i), 0, 0]) for c in range(len(s2[r])) ]
              for r in range(len(s2)) ]

for i in range(9, 181, 9):
    print("Phase shift by:", i, "degrees")
    image2display(show_shift_sine(image2, i))
