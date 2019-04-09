# Author: Kelvin Sung
# Assignment 8: Test cases
# Date: Nov 12, 2018

#   
# Please include the following in your Assignment-8 as test cases for your code
#
import random

random.seed(0)      # to ensure same answer each run
num_patients = -1
num_features = -1

print("*******************************************************************")
print("************** REMEMBER to include: random.seed(0) ***************")
print("*******************************************************************")
#
# A: Data file
def test_read(p, f):
    v, m = read_data("train.data", p, f)
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
    w = rand_vector(f)
    print("      Random vector:", w)
    print("      fraction_wrong(A, u, w=Rand):", fraction_wrong(pmat, pvec, w))

print("E: Testing utilities: fraction_wrong(A, b, w)")
test_fraction_wrong(3, 3, pvec3, pmat3x3)
test_fraction_wrong(7, 13, pvec7, pmat7x13)
test_fraction_wrong(20, 4, pvec20, pmat20x4)
test_fraction_wrong(20, 22, pvec20, pmat20x22)
test_fraction_wrong(len(pvec), len(pmat[0]), pvec, pmat)
test_fraction_wrong(len(pvec), len(pmat[0]), pvec, pmat)
print("=========> End of E: <===================")


