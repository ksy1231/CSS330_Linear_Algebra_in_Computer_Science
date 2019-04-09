# Author: Soo Yun Kim
# Quiz 9: Solution
# Date: Dec 10, 2018
    
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
    return [random.randrange(-8, 8) for i in range(size)]


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

def print_vector(v, msg, space):
    print(f"{msg:>{space}}=", end='')
    for i in range(len(v)):
        print(f"{v[i]:>8.4} ", end='')
    print()

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
    student_mat = list()
    file = open(fname)
    for line in file:
        if (line[0] != '#'):
            row = line.split(",")
            # row[0] is patient ID, ignore
            # row[1] is diagonsis: store in result_vec
            # result_vec.append(-1 if row[1]=='B' else +1)
            result_vec.append(float(row[1]))
            r_vec = [float(row[v]) for v in range(2, col_count+2, 1)]
            student_mat.append(r_vec)
            row_count = row_count - 1
            if row_count == 0:
                return result_vec, student_mat
    return result_vec, student_mat


#   Task 8.4.2
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
    Computation result:
         Performing simple dot-product:
              Dot-r = Row-r-in-A dot w
         if Dot-r has same sign as b[r]
              Correct++
         else
              InCorrect++
         Returns:
              InCorrect/R  [R is the total number of patients]
    The returned result tells us, with the given W-"hypothesis vector" [of which
      feature to examine], what is the error

    '''
    p_vec = mat_vec(A, w)      # RxC  mul C ==> p_vec is of R-Dimension
    s_vec = signum(p_vec)      # s_vec +1 if positive, else -1
    # print("p-vec", p_vec)
    # print("s_vec=", s_vec)
    nD = num_diff(s_vec, b)
    return nD/len(s_vec)


# Task 8.4.4
def loss(A, b, w):
   ''' A: RxC is the mat_dict: each row is a patient, columns are the features
           Refer to this as matrix with "Feature vectors"
           There are R-number of patients
           There are C-number of featuers per patient
        b: a R-vector [number of patients in the A matrix]
           Each entire is a +1 (malignant) or -1 (benign)
        w: a C-vector (number of features recorded per patient, 30 in this case)
           each entry is a +1 (should use) or -1, should not use
           w-vector tells which of the features should be used in predicting
    computes and returns
         Square of [ Size(Aw - b) ]
    '''
   p_vec = mat_vec(A, w)        # RxC mul C => p_vec is of R-Dimension
   x_vec = sub_vector(p_vec, b)
   return dot_vector(x_vec, x_vec)


# Task 8.4.9
def find_gradient(A, AT, b, w):
    p_vec = mat_vec(A, w)
    x_vec = scale_vector(2, sub_vector(p_vec, b))
    return mat_vec(AT, x_vec)


# Task 8.4.10
def gradient_descent_step(A, AT, b, w, sigma):
    g = find_gradient(A, AT, b, w)
    newV = add_vector(w, scale_vector(-sigma, g))
    #print("Step:")
    #print("   g=", g)
    #print("   newV=", newV)
    return newV


# Task 8.4.11
def gradient_descent(A, AT, b, w, sigma, T):
    error_step = 0
    for i in range(T):
        w = gradient_descent_step(A, AT, b, w, sigma)
        #print(f"{i}: Desceint")
        #print(w)
        error_step = error_step + 1
        if error_step == print_frequency:
            # print(w)
            print(f"\n ********** iteration step={i}  Loss={loss(A, b, w)}********")
            error_step = 0
    return w


# ********* BEGIN TESTING ****************


max_students = 137
max_features = 17

sigma = 0.0000001
training_cycles = 999999
print_frequency = 1000
num_students = 1
num_features = 1

while training_cycles > 1:
    print("")
    print(f"Training data: max students={max_students}, max features={max_features}")
    user_input = input("Please enter: number of students, features, cycles to train the system, and print interval: ")
    input_list = user_input.split(',')
    num_students = min(int(input_list[0]), max_students)
    num_features = min(int(input_list[1]), max_features)
    training_cycles = int(input_list[2])
    print_frequency = int(input_list[3])
    print(f"students:{num_students}, Features:{num_features}, Training Cycles:{training_cycles}, Print interval:{print_frequency}")
    if training_cycles > 0:
        pvec, pmat = read_data("train.data.txt", num_students, num_features)
        pmat_trans = transpose_mat(pmat)

        w = set_vector(1, num_features)
        w = gradient_descent(pmat, pmat_trans, pvec, w, sigma, training_cycles)
        print(f"Training result: ", w)
        print("With training data, Aw=", mat_vec(pmat, w))
        print("Data from source file, b=", pvec)
        print(f"Loss={loss(pmat, pvec, w)}")
        
        # Now open and try the actual 
        pvec, pmat = read_data("verify.data.txt", 20, num_features)
        pmat_trans = transpose_mat(pmat)
        total_error = 0

        for i in range(20):
            e = dot_vector(pmat[i], w) - pvec[i]
            error = e * e
            print(f"{i}-th student: data says= {pvec[i]} our prediction={dot_vector(pmat[i], w):.2f}, loss={error:.2f}")
            total_error = total_error + error

        print(f"Total error: {total_error:.2f}")
       
