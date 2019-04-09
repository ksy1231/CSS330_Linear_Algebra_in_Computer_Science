# Author: Soo Yun Kim
# Assignment 8
# Date: Nov 30, 2018

#   
# Please include the following in your Assignment-8 as test cases for your code
#
# Import the necessary libraries
import random
import traceback
    # https://docs.python.org/3/library/traceback.html

random.seed(0)      # to ensure same answer each run
num_patients = -1
num_features = -1

print("*******************************************************************")
print("************** REMEMBER to include: random.seed(0) ***************")
print("*******************************************************************")
#
# A: Data file
def read_data(fname, num_patient, num_features):
    '''
    '''
    pvec = list()
    pmat = list()
    file = open(fname)
    for line in file:
        row = line.split(",")
        # row[0] is patient ID, ignore
        # row[1] is diagonsis: store in pvec
        pvec.append(-1 if row[1]=='B' else +1)
        r_vec = [float(row[v]) for v in range(2, 2 + num_features)]
        pmat.append(r_vec)
    return pvec[:num_patient], pmat[:num_patient]

def test_read(p, f):
    v, m = read_data("train.data.txt", p, f)
    print(f"Testing reading: num_patients={p}  num_features={f}")
    print(f"    pvec{p}:", v)
    print(f"    pmat{p}x{f}:", m)
    print()
    return v, m

print("A: Testing data file reading")
pvec3, pmat3x3 = test_read(3, 3)
pvec7, pmat7x13 = test_read(7, 13)
pvec20, pmat20x4 = test_read(20, 4)
pvec20, pmat20x22 = test_read(20, 22)
pvec, pmat = test_read(num_patients, num_features)
print("=========> End of A: <===================")
print("\n\n")

def set_vector(value, size):
    l = list()
    for i in range(size):
        l.append(value)
    return l
    
def rand_vector(size):
    l = list()
    for i in range(size):
        l.append(random.randrange(-8, 8))
    return l

def scale_vector(alpha, v):
    return [alpha * i for i in v]

#B: Generalized vector support .....
print("B: Testing generalized vector support")
A = set_vector(1, 7)
B = set_vector(-1, 13)
C = rand_vector(7)
D = rand_vector(13)
E = scale_vector(2, A)
F = scale_vector(3.2, D)
print("A=", A)
print("B=", B)
print("C=", C)
print("D=", D)
print("E=", E)
print("F=", F)
print("=========> End of B: <===================")
print("\n\n")

def add_vector(v1, v2):
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return [x + y for x, y in zip(v1, v2)]

def sub_vector(v1, v2):
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return [x - y for x, y in zip(v1, v2)]

def dot_vector(v1, v2):
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return sum(a*b for a, b in zip(v1, v2))

print("C: Testing generalized vector operators")
print("A+C: ", add_vector(A, C))
print("D-B: ", sub_vector(D, B))
print("F.B: ", dot_vector(F, B))
print("A+B: ", add_vector(A, B))
print("D-C: ", sub_vector(D, C))
print("A.B: ", dot_vector(A, B))
print("=========> End of C: <===================")
print("\n\n")

def transpose_mat(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def col_vec(m, i):  # create column vectors
    return [m[r][i] for r in range(len(m))]

def mat_mat(m1, m2):
    try:
        assert(len(m1[0]) == len(m2))
    except AssertionError:
        print(f"!!ERROR!!: illegal lengths! ({len(m1[0])}, {len(m2)})")
        traceback.print_stack(None, 2)
        return []
    return [ [dot_vector(m1[i], col_vec(m2, j)) for j in range(len(m2[0]))]
                 for i in range(len(m1)) ]

def mat_vec(m, v):
    try:
        assert(len(m[0]) == len(v))
    except AssertionError:
        print(f"!!ERROR!!: illegal lengths! ({len(m[0])}, {len(v)})")
        traceback.print_stack(None, 2)
        return []
    return [dot_vector(m[i], v) for i in range(len(m))]

print("D: Testing generalized matrix operators")
M = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
Ma = transpose_mat(pmat3x3)
Mb = transpose_mat(pmat20x4)
print("M=", M)
print("transpose_mat(M):", transpose_mat(M))
print("transpose_mat(pmat3x3):", Ma)
print("transpose_mat(pmat20x4):", Mb)
print("mat_mat(pmat3x3, Ma):", mat_mat(pmat3x3, Ma))
print("mat_mat(pmat20x4, Mb):", mat_mat(pmat20x4, Mb))
print("mat_mat(Mb, pmat20x4):", mat_mat(Mb, pmat20x4))
print("mat_vec(pmat3x3, pvec3):", mat_vec(pmat3x3, pvec3))
print("mat_vec(pmat20x22, pvec20):", mat_vec(pmat20x22, pvec20))
print("mat_mat(pmat20x4, pmat3x3):", mat_mat(pmat20x4, pmat3x3))
print("mat_vec(pmat20x4, pvec3):", mat_vec(pmat20x4, pvec3))
print("mat_vec(pmat3x3, pvec20):", mat_vec(pmat3x3, pvec20))
print("=========> End of D: <===================")
print("\n\n")

def signum(u):
     return [-1 if u[i] < 0 else +1 for i in range(len(u))]

def num_diff(u, v):
    try:
        assert(len(u) == len(v))
    except AssertionError:
        print(f"!!ERROR!!: illegal lengths! {len(u)} != {len(v)}")
        traceback.print_stack(None, 2)
        return 0
    count = 0
    for i in range(len(u)):
         if u[i] != v[i]:
             count = count + 1
    return float(count)
     
print("E: Testing utilities: signum(u)")
A = rand_vector(3)
sA = signum(A)
print("           A=", A)
print("   signum(A):", sA)
B = rand_vector(7)
sB = signum(B)
print("           B=", B)
print("   signum(B):", sB)
C = rand_vector(16)
sC = signum(C)
print("           C=", C)
print("   signum(C):", sC)

print("E: Testing utilities: num_diff(u, v)")
print("   diff(sA, -1):", num_diff(sA, set_vector(-1, 3)))
print("   diff(sA,  1):", num_diff(sA, set_vector( 1, 3)))
print("   diff(sB, -1):", num_diff(sB, set_vector(-1, 7)))
print("   diff(sB,  1):", num_diff(sB, set_vector( 1, 7)))
print("   diff(sC, -1):", num_diff(sC, set_vector(-1, 16)))
print("   diff(sC,  1):", num_diff(sC, set_vector( 1, 16)))
sD = signum(rand_vector(7))
sE = signum(rand_vector(7))
print("   sD=", sD)
print("   diff(sB,  sD):", num_diff(sB, sD))
print("   sE=", sE)
print("   diff(sB,  sE):", num_diff(sB, sE))
print("=========> End of E: <===================")


