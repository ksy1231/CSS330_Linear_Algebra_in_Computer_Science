# Author: Soo Yun Kim
# Assignment 9 A to C test cases 
# Date: Dec 7, 2018
    
# Import the necessary libraries

from Lib_From_AS8 import *

pvec3, pmat3x3 = read_data("train.data.txt", 3, 3)
pvec7, pmat7x13 = read_data("train.data.txt", 7, 13)
pvec20, pmat20x22 = read_data("train.data.txt", 20, 22)
pvec, pmat = read_data("train.data.txt", -1, -1)

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
     return num_diff(signum(mat_vec(A, w)), b) / len(b)

# ********* BEGIN TESTING ****************

# First thing first, lets verfiy fraction_wrong() is running correctly
def test_fraction_wrong(n, f, pvec, pmat):
    print(f"   With {n} patients and {f} features")
    print(f"   pvec{n}=", pvec)
    w = set_vector(1, f)
    print("      fraction_wrong(A, u, w=+1)  :", fraction_wrong(pmat, pvec, w))
    w = set_vector(-1, f)
    print("      fraction_wrong(A, u, w=-1)  :", fraction_wrong(pmat, pvec, w))
    w = rand_vector(f)
    print("      Random vector:", w)
    print("      fraction_wrong(A, u, w=Rand):", fraction_wrong(pmat, pvec, w))

print("A: Testing utilities: fraction_wrong(A, b, w)")
test_fraction_wrong(3, 3, pvec3, pmat3x3)
test_fraction_wrong(7, 13, pvec7, pmat7x13)
test_fraction_wrong(20, 22, pvec20, pmat20x22)
print("=========> End of A: <===================")


A = [ [1, 2], [3, 4], [5, 6]]
AT = transpose_mat(A)
b = [1, 2, 3]

def loss(A, b, w):
     result = sub_vector(mat_vec(A, w), b)
     return dot_vector(result, result)

# Now lets verfiy loss() is running correctly
def test_loss(n, f, pvec, pmat):
    print(f"   With {n} patients and {f} features")
    print(f"   pvec{n}=", pvec)
    w = set_vector(1, f)
    print("      loss(A, u, w=+1)  :", loss(pmat, pvec, w))
    w = set_vector(-1, f)
    print("      loss(A, u, w=-1)  :", loss(pmat, pvec, w))
    w = rand_vector(f)
    print("      Random vector:", w)
    print("      loss(A, u, w=Rand):", loss(pmat, pvec, w))
    
print("\n\nB: Testing utilities: loss(A, b, w)")
print("   With simple case A=", A)
print("                    b=", b)
test_loss(3, 2, b, A)
test_loss(3, 3, pvec3, pmat3x3)
test_loss(7, 13, pvec7, pmat7x13)
test_loss(20, 22, pvec20, pmat20x22)
print("=========> End of B: <===================")



pmat3x3T = transpose_mat(pmat3x3)
pmat7x13T = transpose_mat(pmat7x13)
pmat20x22T = transpose_mat(pmat20x22)

def find_gradient(A, AT, b, w):
     Aw = mat_vec(A, w)
     _2AT = [ [2*AT[r][c] for c in range(len(AT[0]))] for r in range(len(AT))]
     return mat_vec(_2AT, sub_vector(Aw, b))

# Now lets verfiy find_gradient() is running correctly
def test_find_gradient(n, f, pvec, pmat, pmatT):
    print(f"   With {n} patients and {f} features")
    print(f"   pvec{n}=", pvec)
    w = set_vector(1, f)
    print("      find_gradient(A, AT, u, w=+1)  :", find_gradient(pmat, pmatT, pvec, w))
    w = set_vector(-1, f)
    print("      find_gradient(A, AT, u, w=-1)  :", find_gradient(pmat, pmatT, pvec, w))
    w = rand_vector(f)
    print("      Random vector:", w)
    print("      find_gradient(A, AT, u, w=Rand)  :", find_gradient(pmat, pmatT, pvec, w))
    
    
print("\n\nC: Testing utilities: find_gradient(A, AT, b, w)")
print("   With simple case A=", A)
print("                    b=", b)
test_find_gradient(3, 2, b, A, AT)
test_find_gradient(3, 3, pvec3, pmat3x3, pmat3x3T)
test_find_gradient(7, 13, pvec7, pmat7x13, pmat7x13T)
test_find_gradient(20, 22, pvec20, pmat20x22, pmat20x22T)
print("=========> End of C: <===================")


# ************ End of testing, begin of actual solution


max_patients = 300
max_features = 30

sigma = 0.000000001   # DO NOT CHANGE THIS!!
T = 2
Check_Step = 1
num_patients = 1
num_features = 1

def gradient_descent_step(A, b, w):
     g = find_gradient(A, transpose_mat(A), b, w)
     result = [sigma*g[i] for i in range(len(g))]
     return sub_vector(w, result)

while T > 1:
    print("")
    print(f"Training data: max patients={max_patients}, max features={max_features}")
    user_input = input("Please enter: number of patients, features, printing frequency and cycles to train the system: ")
    input_list = user_input.split(',')
    num_patients = min(int(input_list[0]), max_patients)
    num_features = min(int(input_list[1]), max_features)
    Check_Step = int(input_list[2])
    T = int(input_list[3])
    print(f"Patients:{num_patients}, Features:{num_features}, Training Cycles:{T}")
    if T > 0:
        w = set_vector(0.1, num_features)  # Please keep this initial guess ...
        rvec, pmat = read_data("train.data.txt", num_patients, num_features)
        pmat_trans = transpose_mat(pmat)

        step = 0
        for i in range(T):
             w = gradient_descent_step(pmat, rvec, w)
             wrong_fraction = fraction_wrong(pmat, rvec, w)
             Loss = loss(pmat, rvec, w)
             step = step + 1
             if step == Check_Step:
                  print(f"   iteration step={i}  Wrong_Fraction={wrong_fraction:.5f}   Loss={Loss}")
                  step = 0
             
        # this is where you will call gradient_descent() to compute w
        print("Training result:", w)
        print("With training data ... fraction_wrong=", fraction_wrong(pmat, rvec, w))
        
        # Now open and try the actual 
        rvec, pmat = read_data("validate.data.txt", -1, num_features)
        print("With validate data ... fraction_wrong=", fraction_wrong(pmat, rvec, w))
        
print("Thanks for trying, Bye")


