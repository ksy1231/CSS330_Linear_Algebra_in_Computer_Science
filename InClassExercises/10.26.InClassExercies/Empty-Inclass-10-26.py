# Author: 
# Attempt at class exercise 10/26
#

# make sure to import math and the sin function
# pi is math.pi
import math
from math import sin

# setup importa path to include ./Lib
import sys
sys.path.append('./Lib')  # this is where all the library files are

# import reading of PNG image file into image structure
# After opening an image:
#   image[row][column]
#   len(image) says how many rows [y-size, or height]
#   len(image[0]) says how many column [x-size, or width]

# Here are the three utilities you can use, the last one is just in case
# I did not use the last function
from image_mat_util import file2image
from image_mat_util import image2display
from image_mat_util import image2file  # in case you want to save to a file

image = file2image("SourceImages/s3-256.png")
image2display(image)

