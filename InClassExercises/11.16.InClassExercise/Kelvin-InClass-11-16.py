# Author: Kelvin Sung
# Inclass Exercise
# Date: Nov 12, 2018
    
# Import the necessary libraries
import random
import traceback
    # https://docs.python.org/3/library/traceback.html

def read_data(fname):
    '''
    '''
    result_vec = list()
    patient_mat = list()
    file = open(fname)
    for line in file:
        row = line.split(",")
        # row[0] is patient ID, ignore
        # row[1] is diagonsis: store in result_vec
        result_vec.append(-1 if row[1]=='B' else +1)
        r_vec = [float(row[v]) for v in range(2, len(row))]
        patient_mat.append(r_vec)
    return result_vec, patient_mat


def add_last_element(v1, v2):
    try:
        assert(len(v1) == len(v2))
    except AssertionError:
        print(f"!!ERROR!!: {len(v1)} != {len(v2)}")
        traceback.print_stack(None, 2)
        return 0
    return v1[len(v1)-1] + v2[len(v1)-1]

def test_random():
    l = list()
    for i in range(10):
        l.append(random.randrange(-8, 8))
    return l

print("A: Understanding seed and testing random")
print("   10 random numbers without seed call :", test_random())
print("   10 random numbers without seed call :", test_random())
print("   10 random numbers without seed call :", test_random())
random.seed(0)
print("   10 random numbers after seed(0) call: ", test_random())
random.seed(0)
print("   10 random numbers after seed(0) call: ", test_random())
random.seed(0)
print("   10 random numbers after seed(0) call: ", test_random())
print("Take away: after a seed() call, we reset random number generation")
print("    Good way to get predictable/repeatable random numbres")
print()

print("B: Understanding assert")
v1 = [1, 2, 3, 4, 5]
v2 = [2, 3, 4, 5, 6]
v3 = [1, 2, 3]
print("V1=", v1)
print("V2=", v2)
print("V3=", v3)
print("add_last_element(v1, v1):", add_last_element(v1, v1))
print("add_last_element(v1, v2):", add_last_element(v1, v2))
print("add_last_element(v1, v3):", add_last_element(v1, v3))
print("Notice: traceback.print_stack prints from where the function call occured")
print("         also, we can continue to execute after the assertion failure")
print()

print("C: Reading data file")
pvec, pmat = read_data("my.data.txt")
print("    vec=", pvec)
print("    mat=", pmat)
print("Notice: we can have two return values from the read_data function")
