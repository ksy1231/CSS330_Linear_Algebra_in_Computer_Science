#
print("Soo Yun Kim")
print("Oct 4, 2018")
print("Solution for Assignment #1")
print("---------------------------")

#
# Task 0.5.8
#
a = {x*y for x in {1, 9, 3} for y in {2, 6, 18}}
print("Answer to Task 0.5.8:", a, "[note: overlapping sets result in five-element set]")
print()

#
# Task 0.5.11
#
L = ['A', 'B', 'C']
N = [1, 2, 3]
a = [[x,y] for x in ['A', 'B', 'C'] for y in [1,2,3]]
print("Answer to Task 0.5.11:", a)
print()

#
# Task 0.5.14
#
S = {-4, -2, 1, 2, 5, 0}
a = [(i,j,k) for i in S for j in S for k in S if (i+j+k) ==0]
print("Answer to Task 0.5.14:", a)
print()

#
# Task 0.5.20
#
L1 = [10, 25, 40]
L2 = [1, 15, 20]
a = [i+j for (i, j) in zip([10, 25, 40], [1, 15, 20])]
print("Answer to Task 0.5.20:", a)
print()

#
# Task 0.5.24
#
D = {'red', 'white', 'blue'}
a = {x:x for x in D}
print("Answer to Task 0.5.24:", a)
print()

#
# Task 0.5.26
#
id2salary = { 0: 10000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', '', 'Moe']
a = {names[x]:y for (x,y) in id2salary.items() if x < len(names)}
print("Answer to Task 0.5.26:", a)
print()

#
# Task 0.5.30
#
D = {'a': 'A', 'b':'B', 'c':'C'}
keys = ['b', 'c', 'a']
def dict2list(dct, keylist): return [dct[key] for key in keylist]
a = dict2list(D, keys)
print("Answer to Task 0.5.30:", a)
print("")
print("")

#
# Problem 0.8.4
#
D = {'thank you': 'merci', 'goodbye': 'au revoir'}
def inv_dict(d): return dict([v,k] for k,v in d.items())
a = inv_dict(D)
print("Answer to Problem 0.8.4: a:", a)
print()

