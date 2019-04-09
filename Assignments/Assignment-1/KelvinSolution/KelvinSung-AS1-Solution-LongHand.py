#
print("Kelvin Sung")
print("Sep 15, 2018")
print("Solution for Assignment #1 (With explicit loop implementation)")
print("--------------------------------------------------------------")

#
# Task 0.5.8
#
w = 4 # w > 2 to ensure no overlapping between the two set
p = 2
a = {x*y for x in {0, 1, p} for y in {w, p*w, p*p*w}}
# one answer set:
#    set 1 = {0, 1, p}
#        0: will appear in output
#        1: says, the three numbers of next set will all show
#        p: says, the next set's numbers must be: {a=w, b=p*a, c=p*b}
# ==> the resulting set is: {0, a, b, c, p*c}
#
# e.g., {0, 1, 2} works with {4, 8, 16}  // p==2 and w==4
#       output is {0, 4, 8, 16, 32}
#
# Lesson: sometimes tricky questions can be logically broken down into simple math and algorithm
#
print("Answer to Task 0.5.8:", a, "[note: overlapping sets result in five-element set]")
def longhand(p, w):
    r = set()  # note: how to create a typed empty set: works for "list", tuple, .... 
    for x in {0, 1, p}:
        for y in [w, p*w, p*p*w]:
            r = r | {x*y}
    return r
print("   explicit funciton:", longhand(p, w))
print(" ")


#
# Task 0.5.11 (Page 23)
# Write a double list comprehension over the list ['A', 'B', 'C'] and [1, 2, 3]
# whose value is the list of all possible two-element lists [letter, number]. 
#
# Lesson: how to iterate (nested loop)
#
L = ['A', 'B', 'C']
N = [1, 2, 3]
a = [[x , y] for x in L for y in N]
print("Answer to Task 0.5.11:", a)
def longhand(L, N):
    r = list()
    for x in L:
        for y in N:
            r = r + [[x, y]]  # note: with [x,y] ==> results in x, and y being new members of list
    return r
print("    explicit funciton:", longhand(L, N))
print("")


#
# Task 0.5.14 (Page 25)
# Suppose S is a set of intergers (e.g., {-4, -2, 1, 2, 5, 0}. Write a triple
# comprehsension whose value is a list of all three-element tuples (i, j, k) such that i, j, k
# are elements of S whose sum is zero
#
# Lesson: nested iterations with conditions
#
S = {-4, -2, 1, 2, 5, 0}
a = [(x, y, z) for x in S for y in S for z in S if (x+y+z == 0)]
print("Answer to Task 0.5.14:", a)
def longhand(S):
    r = list()
    for x in S:
        for y in S:
            for z in S:
                if x+y+z == 0:
                    r = r + [(x, y, z)]
    return r
print("    explicit funciton:", longhand(S))
print("")


#
# Task 0.5.20 (Page 27)
# Startin from the lists [10, 25, 40] and [1, 15, 20], write a comprehension
# whose value is the three-element list in which the first element is the sum of 10 and 1,
# the second is the sum of 25 and 15, and the third is the sum of 40 and 20. Y our expression
# should use zip but not list.
#
# Lesson: transform into data type that is convenient to work with before iterate
# 
L1 = [10, 25, 40]
L2 = [1, 15, 20]
a = [x+y for (x, y) in zip(L1, L2)]
print("Answer to Task 0.5.20:", a)
def longhand(L1, L2):
    r = list()
    for i in range(len(L1)):
        r = r + [L1[i]+L2[i]]
    return r
print("    explicit funciton:", longhand(L1, L2))
def longhand(L1, L2):
    r = list()
    z = zip(L1, L2)
    for i in z:
        r = r + [i[0]+i[1]]  # each i is (a, b) ==> i[0] is a
    return r
print("    explicit funciton:", longhand(L1, L2))
print("")



#
# Task 0.5.24 (Page 29)
# Assign some set to the variable D (e.g., D=...) Now, write a comprehension that evalutes
# to a dictionary that represents the identity function on D.
#
# Lesson: get to know what is a dictionary, review what is Identity
#
D = {'red', 'white', 'blue'}
a = {k: k for k in D}
print("Answer to Task 0.5.24:", a)
def longhand(D):
    r = dict()
    for i in D:
        r[i] = i
    return r
print("    explicit funciton:", longhand(D))
print("")

#
# Task 0.5.26 (Page 30)
# Suppose d is a dictionary that maps some employee IDs (a subset of the integers from 0 to n-1)
# to salaries. Suppose L is an n-element list whos ith element is the name of employee number i.
# Your goal is to write a comprehension whose value is a dictionary mapping employee names to salaries.
# You can assume that employee names are distinct.
#
# Lesson: learn to work with dictionary, remember about the if/else
#             condition in the end: will not return a value
#             condition in the front, always return something
id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', '', 'Moe']
a = {names[n]: id2salary[n] if n in id2salary else 0 for n in range(len(names))}
            # NOTE: AH!! the "if" can be infront of the for loop!!
print("Answer to Task 0.5.26:", a)
def longhand(idSalary, names):
    r = dict()
    for n in range(len(names)):
        if n in idSalary:
            r[names[n]] = idSalary[n]
            # print(r, n, idSalary[n], names[n])
        else:
            r[names[n]] = 0
    return r
print("    explicit funciton:", longhand(id2salary, names))
print("")



#
# Task 0.5.30 (Page 31)
# Define a one-line procedure dict2list(dct, keylist) with
#     input: dictionary dct,
#            keylist: consists of keys to the dictionary
#    output: list L such that L[i] = keylist[i]
#
# Lesson: What is a procedure (both in Python's sense, and in "math" sense
#          ==> Implementation of a specification [an algorithm]
#
def d2l(dict, keylist): return [dict[elm] for elm in keylist]
D = {'a': 'A', 'b':'B', 'c':'C'}
keys = ['b', 'c', 'a']
a = d2l(D, keys)
print("Answer to Task 0.5.30:", a)
def longhand(dict, keylist):
    r = list()
    for elm in keylist:
        r = r + [dict[elm]]
    return r
print("    explicit funciton:", longhand(D, keys))

print("")
print("")



#
# Problem 0.8.4 (Page 37)
# invert the key/value pair such that keys are value and values are keys
#
# Lesson: familiarization with dictionary and procedure
#
def inv_dict(dict):
    return { dict[k]: k for k in dict.keys() }
    # this works, but ugly: return {list(dict.values())[n]: list(dict.keys())[n] for n in range(len(dict))}

# do inv_dict long hand
def id(dict) :
    v = list(dict.values())
    k = list(dict.keys())
    nd = {}
    for n in range(len(v)):
        nd[v[n]] = k[n]
        # cannot do this for dictionary: nd += {v[n]: k[n]}
    return nd

D = {'thank you': 'merci', 'goodbye': 'au revoir'}
a = inv_dict(D)
b = id(D)
print("Answer to Problem 0.8.4: a:", a)
print("                       : b:", b)




#
# Problem 0.8.5
#   row(p, n): create a list [p, p+1, p+2 ... p+n-1]
# Now, write a comprehension whose value is a 15-element list of 20-element lists such that
# the jth element of the ith list is i+j. You can use row(p, n) in your comprehension.
# Now, write the same comprehension but without using row(p, n).
#
# Lesson:
#     Part a: Can call procedure from a comprehension
#     Part b: Comprehension can contain comprehension
#
def row(p, n):
    return [p+x for x in range(n)]

a = row(10, 4)
print("Answer to Problem 0.8.5: row(10,4):", a)
a = [ row(i, 20) for i in range(15) ]
print("Answer to Problem 0.8.5: a with row: \n", a)
a = [ [i+j for j in range(20)] for i in range(15)]
print("Answer to Problem 0.8.5: a: without row()\n", a)

def r(p, n):
    s = []
    for x in range(n):
        s = s + [p+x]
    return s


def lofl_with_r(l1_size, l2_size) :
    l = list()
    for i in range(l1_size):
        l.append(r(i, l2_size))
    return l


def lofl_no_r(l1_size, l2_size) :
    l = list()
    for i in range(l1_size):
        innerl = list()
        for j in range(l2_size):
            innerl.append(i+j)
        l.append(innerl)
    return l

b = r(10, 4)
print("               Longhand solution  : b:", b)
print("                      with_row    :\n", lofl_with_r(15, 20))
print("                   without_row    :\n", lofl_no_r(15, 20))
