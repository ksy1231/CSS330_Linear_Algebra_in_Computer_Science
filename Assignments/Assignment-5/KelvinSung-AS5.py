## Author: Kelvin Sung
# Assignment 5: Solution
# Date: Oct 2018
# Interpreting colors as vectors and image manipulation via
# vector add/scale
#
import math
from math import sin
import sys
sys.path.append('./Lib')  # this is where all the library files are
from image_mat_util import file2image
from image_mat_util import image2display
from image_mat_util import image2file  # in case you want to save to a file


s1 = file2image("SourceImages/s1-256.png")
s2 = file2image("SourceImages/s2-256.png")
#   image[row][column]
#   len(image) says how many rows [y-size, or height]
#   len(image[0]) says how many column [x-size, or width]
# image2display(m)

def scale_pixel(alpha, p):   # p is a tuple (R G B A)
    return tuple(alpha * i for i in p)

def add_pixel(p1, p2):
    return tuple(a+b for a, b in zip(p1,p2))

def scale_image(alpha, m):
    return [ [scale_pixel(alpha, m[r][c]) for c in range(len(m[r])) ]
              for r in range(len(m)) ]

def add_image(m1, m2):   # assume same resolution!
    return [ [add_pixel(m1[r][c], m2[r][c]) for c in range(len(m1[r])) ]
              for r in range(len(m1)) ]

def color_shift_image(p, m1):   # assume same resolution!
    return [ [add_pixel(p, m1[r][c]) for c in range(len(m1[r])) ]
              for r in range(len(m1)) ]

def cross_blend(min, max, base, steps, m1, m2):
    ext = 1
    for i in range(min, max, steps):
        alpha = i / base
        print(f'Cross blend alpha={alpha} beta={1-alpha}')
        w = add_image(scale_image(alpha, m1), scale_image(1-alpha, m2))
        # image2file(w, f'cb-{ext}.png')
        image2display(w)
        ext = ext + 1

"""
print("Increase image resolution by 2 times")
w = [ [s2[r//2][c//2] for c in range(2*len(s2[0]))]
          for r in range(2*len(s2))]
image2display(w)
input("<CR> for next:")
print("Decrase image resolution by 2 times")
w = [ [ scale_pixel(0.25,
           add_pixel(add_pixel(s2[r-1][c-1], s2[r-1][c]),
                     add_pixel(s2[r][c-1], s2[r][c])))
           for c in range(1, len(s2[0]), 2)]
              for r in range(1, len(s2), 2)]
image2display(w)
"""

print()
input("<CR> to see A: Convex sum, from 0 to 1, in steps of 0.1")
cross_blend(0, 11, 10, 1, s1, s2)

print()
input("<CR> to see B: Affine sum, from 1 to 2, in steps of 0.1")
cross_blend(10, 21, 10, 1, s1, s2)

print()
print("<CR> to see C: Brighten image to 500% in 10 steps")
a = scale_image(0.2, s2)
for i in range(0, 11, 1):
    alpha = 1 + 4*i/10
    print(f'Alpha={alpha}')
    w = scale_image(alpha, a)
    image2display(w)


print()
input("<CR> to see D: Shift image RGBA to 250 in 10 steps")
for i in range(25, 260, 25):
    alpha = (i, i, i, i)
    print(f'Shift alpha={alpha}')
    w = color_shift_image(alpha, s2)
    image2display(w)
    

print()
print("<CR> to see E: Shift image R-Channel to 5 in 10 steps")
for i in range(0, 250, 25):
    alpha = (-i, 0, 0, 0)
    print(f'Shift alpha={alpha}')
    w = color_shift_image(alpha, s2)
    image2display(w)

    
print("<CR> to see F: Continue to shift image G-Channel to 5 in 10 steps")
a = color_shift_image((-250, 0, 0), s2)
for i in range(0, 250, 25):
    alpha = (0, -i, 0, 0)
    print(f'Shift alpha={alpha}')
    w = color_shift_image(alpha, a)
    image2display(w)


print()
print("<CR> to see G: Darken image to 50% in 10 steps")
for i in range(0, 11, 1):
    alpha = 1 - i/10
    print(f'Alpha={alpha}')
    w = scale_image(alpha, s2)
    image2display(w)


# Sine wave:
# Amplitude=100
# Period = 2 * (2 * PI * Image-Width) == len(m[0])
amp = 100
omega = 2 * 2 * math.pi / len(s2[0])
def mySine(x):
    return amp * sin(x * omega)

def sine_vector(w):   # assume same resolution!
    return [ mySine(c) for c in range(w) ]
              
print()
print("<CR> to see H: Modulate R-Channel in by sine function:")
def sine_modulate_R(xOffset, rvec, m): 
    width = len(s2[0])
    w = [ [add_pixel((rvec[(c-xOffset)%width], 0, 0, 0), s2[r][c]) for c in range(width)]
          for r in range(len(s2))]
    image2display(w)

width = len(s2[0])
rvec = sine_vector(width)
for i in range(0, 10, 1):
    alpha = int(i * width * 0.25 / 10)
    sine_modulate_R(alpha, rvec, s2)
