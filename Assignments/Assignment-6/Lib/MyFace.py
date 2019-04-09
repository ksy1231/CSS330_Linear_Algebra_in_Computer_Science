# Author: Kelvin Sung
# Date: Oct 18, 2018
#
# Defines a rather ugly looking face
    
# The face
_eye_color = (0, 0, 0)
_nose_color = (0, 0, 200)
_mouth_color = (255, 200, 200)

__MyFacePoints = [
    # Eyes
    [-80, 120],  # left
    [ 80, 120],  # right
    # Nose
    [ 0, 55],    # 
    [ 0, 45],    #
    [ 0, 35],    #
    [-6, 30],    # bottom two holes
    [ 6, 30],    #
    # Mouth
    [-70, -25],  # left-top dot
    [-55, -45],  #
    [-35, -52],  #
    [-15, -55],  #
    [  0, -55],  #  center
    [ 70, -25],  # 
    [ 55, -45],  #
    [ 35, -52],  #
    [ 15, -55]   #
]

__MyFaceSizes = [
    # Eyes
    20, # left
    20, # right
    # Nose
    10,   # 
    10,   #
    10,   #
    10,   # bottom two holes
    10,   #
    # Mouth
    10,   # left-top dot
    10,   #
    10,   #
    10,   #
    10,   #  center
    10,   # 
    10,   #
    10,   #
    10   #
]

__MyFaceColors = [
    # Eyes
    _eye_color,  # left
    _eye_color,  # right
    # Nose
    _nose_color,  # 
    _nose_color,  #
    _nose_color,  #
    _nose_color,  # bottom two holes
    _nose_color,  #
    # Mouth
    _mouth_color,  # left-top dot
    _mouth_color,  #
    _mouth_color,  #
    _mouth_color,  #
    _mouth_color,  #  center
    _mouth_color,  # 
    _mouth_color,  #
    _mouth_color,  #
    _mouth_color  #
]

def myface_pt_list():
    return [p for p in __MyFacePoints]

def myface_size_list():
    return [s for s in __MyFaceSizes]

def myface_color_list():
    return [c for c in __MyFaceColors]

def getMyFace() :
    return myface_pt_list(), myface_size_list(), myface_color_list()
