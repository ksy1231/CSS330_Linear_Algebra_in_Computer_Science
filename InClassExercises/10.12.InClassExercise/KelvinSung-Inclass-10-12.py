#
# Kelvin Sung
# Attempt at Class Exercise 10/12
#
f = open("MyDataFile.txt")
list = list(f)
dict = dict()
for l in list:
    al = l.split()
    #print('Raw data is:', al)
    #print(f'Name:{al[0]:8} Position:{al[1]:8} Comment:{al[2]:8}')
    dict[al[0]] = [int(al[v]) for v in range(3, len(al))]

oneVector = [1 for v in range(11)]

def dot_product(v1, v2):
    return sum([a*b for (a, b) in zip(v1, v2)])

def analyze_vector(name):
    v = dict[name]
    onePlusNegOne = dot_product(v, v)
    oneSubNegOne = dot_product(v, oneVector)
    oneTwice = onePlusNegOne + oneSubNegOne
    oneCount = oneTwice // 2
    negOneCount = onePlusNegOne - oneCount
    zeroCount = len(v) - onePlusNegOne
    print(f'{name:8}', ": Number of 1:", oneCount, " number of -1:", negOneCount, " number of zero:", zeroCount)


print("===============")
print("Problem 1: here is my dictionary")
for i in dict.keys():
    print(f'Key = {i:9} value={dict[i]}')

print()
print("===============")
print("Problem 2: here is my 11-element one vector")
print(oneVector)

print()
print("===============")
print("Problem 3: testing of dot product")
print("Dot MyName   and   MyName  = ", dot_product(dict['MyName'], dict['MyName']))
print("Dot YourName and YourName  = ", dot_product(dict['YourName'], dict['YourName']))
print("Dot ThisName and ThisName  = ", dot_product(dict['ThisName'], dict['ThisName']))
print("Dot ThatName and ThatName  = ", dot_product(dict['ThatName'], dict['ThatName']))
print("testing dot with oneVector")
print("Dot MyName   and OneVector = ", dot_product(dict['MyName'], oneVector))
print("Dot YourName and OneVector = ", dot_product(dict['YourName'], oneVector))
print("Dot ThisName and OneVector = ", dot_product(dict['ThisName'], oneVector))
print("Dot ThatName and OneVector = ", dot_product(dict['ThatName'], oneVector))

print()
print("===============")
print("Problem 4: Analyze vectors")
analyze_vector('MyName')
analyze_vector('YourName')
analyze_vector('ThisName')
analyze_vector('ThatName')



      

