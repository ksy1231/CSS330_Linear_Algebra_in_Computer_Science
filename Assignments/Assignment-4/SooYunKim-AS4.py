from svg_draw import *
import math  # for math.sin() and math.pi functions

width = 1200
height = 800

eye_color = "(0, 0, 0)"
nose_color = "(0, 0, 200)"
mouth_color = "(255, 200, 200)"
L = [ # Note: each list entry is a "PosInfo" meant for the 
      #       plot_points(L) function of the SVG_Draw Library
      #       A PosInfo has three elements:
      #       [ [x,y], size, "ColorString"]
      #       [x,y]: is the point position
      #       size: is the size of the point
      #       ColorString: (r, g, b) where r,g,b is an integer between 0 and 255
   # Eyes
     [[-80, 120], 20, eye_color] # left
    ,[[ 80, 120], 20, eye_color] # right
  # Nose
    ,[[0, 55], 10, nose_color] # top dot
    ,[[0, 45], 10, nose_color] #
    ,[[0, 35], 10, nose_color] #
    ,[[-6, 30], 10, nose_color] # bottom two holes
    ,[[6, 30], 10, nose_color] #
  # Mouth
    ,[[-70, -25], 10, mouth_color] # left-top dot
    ,[[-55, -45], 10, mouth_color] #
    ,[[-35, -52], 10, mouth_color] #
    ,[[-15, -55], 10, mouth_color] #
    ,[[  0, -55], 10, mouth_color] # center
    ,[[ 70, -25], 10, mouth_color] # 
    ,[[ 55, -45], 10, mouth_color] #
    ,[[ 35, -52], 10, mouth_color] #
    ,[[ 15, -55], 10, mouth_color] #
]

# Problem A
print("A: Showing the face")
create_plot(width, height, True)
plot_points(L)
input("Please type return to continue ...")
print("\n")

# Problem B
print("B: Expansion animation via scaling")
def scale_pt(p, alpha):
    return [p[0]*alpha, p[1]*alpha]

def scale_pt_list(l, alpha):
    return [[scale_pt(i[0], alpha), i[1]*alpha, i[2]] for i in l]

for i in range(1, 30, 1):
    a = scale_pt_list(L, i/30)
    clear_plot(True)
    plot_points(a)
input("Please type return to continue ...")
print("\n")

# Problem C
print("C: Translation in the +X and +Y direction")
def translate_pt(p, delta):
    return [p[0]+delta[0], p[1]+delta[1]]

def translate_pt_list(l, delta):
    return [[translate_pt(i[0], delta), i[1], i[2]] for i in l]

b = []
for i in range(0, 301, 20):
    a = translate_pt_list(L, [i, i])
    clear_plot(True)
    plot_points(a)
    b = a
input("Please type return to continue ...")
print("\n")

# Problem D
print("D: Translation in the -X direction")
d = []
for i in range(0, 601, 20):
    c = translate_pt_list(b, [-i, 0])
    clear_plot(True)
    plot_points(c)
    d = c
input("Please type return to continue ...")
print("\n")

# Problem E
print("E: Translation in the X and -Y direction")
e = []
for i in range(0, 301, 20):
    f = translate_pt_list(d, [i, -i])
    clear_plot(True)
    plot_points(f)
    e = f
input("Please type return to continue ...")
print("\n")

# Problem F
print("F: Shrinking animation via scaling")
for i in range(30, 6, -1):
    g = scale_pt_list(L, i/30)
    clear_plot(True)
    plot_points(g)
input("Please type return to continue ...")
print("\n")

# Problem G
print("G: Sine function with amplitude of 300 and period of 300")
amplitude = 400
period = 300
h = scale_pt_list(L, 0.3)

j = translate_pt_list(h, [-600, 0])
for x in range(0, 1201, 10):
    theta = (x / period) * (2 * math.pi)
    y = amplitude * math.sin(theta)
    k = translate_pt_list(j, [x, y])
    clear_plot(True)
    plot_points(k)

l = translate_pt_list(h, [600, 0])
for x in range(1201, -1, -10):
    theta = (x / period) * (2 * math.pi)
    y = amplitude * math.sin(theta)
    k = translate_pt_list(j, [x, y])
    clear_plot(True)
    plot_points(k)

for x in range(0, 1201, 10):
    theta = (x / period) * (2 * math.pi)
    y = amplitude * math.sin(theta)
    k = translate_pt_list(j, [x, y])
    clear_plot(True)
    plot_points(k)
