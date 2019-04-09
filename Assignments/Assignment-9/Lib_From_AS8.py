# Author: Kelvin Sung
# Assignment 8: Solution
# Date: Nov 12, 2018
    
# Import the necessary libraries   
import traceback
import random

'''-----------------------------
Vector utilities
'''
random.seed(0)

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
