# Author: Kelvin Sung
# Assignment 8: Solution
# Date: Nov 12, 2018
    
# Import the necessary libraries   
import traceback
import random

'''-----------------------------
Vector utilities
'''

def set_vector(value, size):
    '''
    returns a vector with constant value, in size
    '''
    return [value] * size

def rand_vector(size):
    '''
       returns a vector with random numbers between -1 and 1
    '''
    return [random.randint(-8, 8) for i in range(size)]


def add_vector(v1, v2):
    try:
        assert(len(v1) == len(v2))   
    except AssertionError:
        print(f"!!ERROR!!: add_vector: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return [a+b for a,b in zip(v1, v2)]


def sub_vector(v1, v2):  # v1 - v2
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: sub_vector: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return [a-b for a,b in zip(v1, v2)]


def scale_vector(alpha, v):
    return [alpha*a for a in v]


def neg_vector(v):
    return scale_vector(-1, v)

    
def dot_vector(v1, v2):
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: dot_vector: different vector lengths! ({len(v1)}, {len(v2)})")
        traceback.print_stack(None, 2)
        return []
    return sum(a*b for a, b in zip(v1, v2))


'''-----------------------------
Matrix utilities
'''

def identity_mat(n):
    """
    returns the identity matrix in R-n
    """
    return [ [1 if i == j else 0 for i in range(n)] for j in range(n) ]


def mat_vec(m, v):   # 
    """
    Multiplies the matrix to the vector
    """
    try:
        assert(len(m[0]) == len(v))
    except AssertionError:
        print(f"!!ERROR!!: mat_vec: illegal lengths! ({len(m[0])}, {len(v)})")
        traceback.print_stack(None, 2)
        return []
    return [dot_vector(m[r], v) for r in range(len(m))]


def col_vec(m, i):  # create column vectors, i is 0, 1, ...
    return [m[r][i] for r in range(len(m)) ]


def mat_mat(m1, m2):  # two matrices
    try:
        assert(len(m1[0]) == len(m2))
    except AssertionError:
        print(f"!!ERROR!!: mat_mat: illegal lengths! ({len(m1[0])}, {len(m2)})")
        traceback.print_stack(None, 2)
        return []
    return [ [dot_vector(m1[i], col_vec(m2, j)) for j in range(len(m2[0]))]
                 for i in range(len(m1)) ]

def transpose_mat(m):
    return [   [m[r][c] for r in range(len(m)) ]
                   for c in range(len(m[0])) ]

  
def read_data(fname, row_count=-1, col_count=-1):
    '''
    row_count: how many rows to read, -1 means all rows
    col_count: how many columns to read, -1 means all columns

    these are important for testing of data
    '''
    if col_count < 0:
        col_count = 30     # this is all the numbers in each row
    result_vec = list()
    patient_mat = list()
    file = open(fname)
    for line in file:
        row = line.split(",")
        # row[0] is patient ID, ignore
        # row[1] is diagonsis: store in result_vec
        result_vec.append(-1 if row[1]=='B' else +1)
        r_vec = [float(row[v]) for v in range(2, col_count+2, 1)]
        patient_mat.append(r_vec)
        row_count = row_count - 1
        if row_count == 0:
            return result_vec, patient_mat
    return result_vec, patient_mat


#   Task 8.4.2
def signum(u):  
    return [-1 if v<0 else 1 for v in u]


def num_diff(u, v):
    """
       u, v: Vectors containing only 1, and -1
       returns number of entries that are different
       
    Implementation, notice if I have a two vectors: A, and B: of 1 and -1 entries
          A = [1, -1, 1, 1, ...]
          B = [1, -1, -1, -1 ...]
          
    Now, since 1*1 = 1, and -1*-1 = 1  // When corresponding entries are the same, we get a "1"
                                       // When corresponding entries are different, we get a -1                           
    then,
           A dot B == nS - nD    # Number of the same corresponding entries - Number of different corresponding entries
           
    if the Vectors are of dimension N, then, we know
           nS + nD = N
    Or,
           nS = N - nD
    So,
           A dot B == N - 2*nD
           ==> nD = 0.5 * [N - (AdotB)]
    """
    return 0.5 * (len(u) - dot_vector(u, v))


# Task 8.4.3
def fraction_wrong(A, b, w):
    ''' A: RxC is the mat_dict: each row is a patient, columns are the features
           Refer to this as matrix with "Feature vectors"
           There are R-number of patients
           There are C-number of featuers per patient
        b: a R-vector [number of patients in the A matrix]
           Each entire is a +1 (malignant) or -1 (benign)
        w: a C-vector (number of features recorded per patient, 30 in this case)
           each entry is a +1 (should use) or -1, should not use
           w-vector tells which of the features should be used in predicting
    '''
    return 0.0


random.seed(0)      # to ensure same answer each run
num_patients = -1
num_features = -1

print("*******************************************************************")
print("************** REMEMBER to include: random.seed(0) ***************")
print("*******************************************************************")
#
# A: Data file
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

print("C: Testing generalized vector operators")
print("A+C: ", add_vector(A, C))
print("D-B: ", sub_vector(D, B))
print("F.B: ", dot_vector(F, B))
print("A+B: ", add_vector(A, B))
print("D-C: ", sub_vector(D, C))
print("A.B: ", dot_vector(A, B))
print("=========> End of C: <===================")
print("\n\n")

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

def test_fraction_wrong(n, f, pvec, pmat):
    print(f"   With {n} patients and {f} features")
    print(f"   pvec{n}=", pvec)
    w = set_vector(1, f)
    print("      fraction_wrong(A, u, w=+1)  :", fraction_wrong(pmat, pvec, w))
    w = set_vector(-1, f)
    print("      fraction_wrong(A, u, w=-1)  :", fraction_wrong(pmat, pvec, w))
    w = rand_vector(n)
    print("      Random vector:", w)
    print("      fraction_wrong(A, u, w=Rand):", fraction_wrong(pmat, pvec, w))

print("E: Testing utilities: fraction_wrong(A, b, w)")
test_fraction_wrong(3, 3, pvec3, pmat3x3)
test_fraction_wrong(7, 13, pvec7, pmat7x13)
test_fraction_wrong(20, 4, pvec20, pmat20x4)
test_fraction_wrong(20, 22, pvec20, pmat20x22)
test_fraction_wrong(len(pvec), len(pmat[0]), pvec, pmat)
print("=========> End of E: <===================")


