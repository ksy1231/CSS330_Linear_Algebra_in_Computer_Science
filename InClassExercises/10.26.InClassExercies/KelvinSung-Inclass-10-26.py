# Author: Kelvin Sung
# Attempt at class exercise 10/26
#
import math
from math import sin
import sys
sys.path.append('./Lib')  # this is where all the library files are
from image_mat_util import file2image
from image_mat_util import image2display
from image_mat_util import image2file  # in case you want to save to a file


image = file2image("SourceImages/s3-256.png")
#   image[row][column]
#   len(image) says how many rows [y-size, or height]
#   len(image[0]) says how many column [x-size, or width]
# image2display(m)

def scale_pixel(alpha, p):   # p is a tuple (R G B A)
    return tuple(alpha * i for i in p)


def add_pixel(p1, p2):
    return tuple(a+b for a, b in zip(p1,p2))


def color_shift_image(p, m1):   # assume same resolution!
    return [ [add_pixel(p, m1[r][c]) for c in range(len(m1[r])) ]
              for r in range(len(m1)) ]


def scale_image(alpha, m):
    return [ [scale_pixel(alpha, m[r][c]) for c in range(len(m[r])) ]
              for r in range(len(m)) ]



def double_resolution(m):
    return [ [m[r//2][c//2] for c in range(2*len(m[0]))]
          for r in range(2*len(m))]


def half_resolution(m):
    return [ [ scale_pixel(0.25,
                    add_pixel(add_pixel(m[r-1][c-1], m[r-1][c]),
                              add_pixel(m[r][c-1],   m[r][c])))
               for c in range(1, len(m[0]), 2)]
                      for r in range(1, len(m), 2)]    


input("<CR> to see A: Display the entered image")
image2display(image)

print("")
input("<CR> to see B: Color Shift the image by (-255, 0, 0, 0):")
image2display(color_shift_image((-255, 0, 0, 0), image))

print("")
input("<CR> to see C: Scaling the image to 0.6 of oringal color values:")
print("This is original image")
image2display(image)
input("<CR> to continue to see 0.6 scale")
image2display(scale_image(0.6, image))

print("")
input("<CR> to see D: Double the image resolution")
print("This is original image")
image2display(image)
input("<CR> to see twice the image resolution")
image2display(double_resolution(image))

print("")
input("<CR> to see E: Half the image resolution")
print("This is original image")
image2display(image)
input("<CR> to see twice the image resolution")
image2display(half_resolution(image))
