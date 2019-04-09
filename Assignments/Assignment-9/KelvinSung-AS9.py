# Author: Kelvin Sung
# Assignment 9: Solution
# Date: Nov 12, 2018
    
# Import the necessary libraries

from Lib_From_AS8 import *

pvec3, pmat3x3 = read_data("train.data", 3, 3)
pvec7, pmat7x13 = read_data("train.data", 7, 13)
pvec20, pmat20x22 = read_data("train.data", 20, 22)
pvec, pmat = read_data("train.data", -1, -1)


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
        if error_step == Check_Step:
            # print(w)
            print(f"   iteration step={i}  Wrong_Fraction={fraction_wrong(A, b, w):2.5f}   Loss={loss(A, b, w)}")
            error_step = 0
    return w


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

sigma = 0.000000001
T = 999999
Check_Step = 1000
num_patients = 1
num_features = 1

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
        rvec, pmat = read_data("train.data", num_patients, num_features)
        pmat_trans = transpose_mat(pmat)

        w = set_vector(0.1, num_features)
        w = gradient_descent(pmat, pmat_trans, rvec, w, sigma, T)
        print("Training result:", w)
        print("With training data ... fraction_wrong=", fraction_wrong(pmat, rvec, w))
        
        # Now open and try the actual 
        rvec, pmat = read_data("validate.data", -1, num_features)
        print("With validate data ... fraction_wrong=", fraction_wrong(pmat, rvec, w))
        
print("Thanks for trying, Bye")
    


