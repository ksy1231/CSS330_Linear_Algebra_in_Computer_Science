f = open("MyDataFile.txt")
lst = list(f)
bl = []
cl = []
for l in lst:
    al = l.split()
    bl.append(al[0])
    cl.append(al[3:])
    dl = [list(map(int, x)) for x in cl]
dic = dict(zip(bl, dl))

print("===============")
print("Problem 1: here is my dictionary")
for key, value in dic.items():
    print('Key =', key, 'value =', value)
print('\n')
#print("\n".join("{}\t{}".format(k, v) for k, v in dic.items()))

print("===============")
print('Problem 2: here is my 11-element one vector')
oneVector = [1 for v in range(11)]
print(oneVector)
print('\n')

print("===============")
print('Problem 3: testing of dot product')

def dot_product(v1, v2):
    new_lst = [x * y for x, y in zip(v1, v2)]
    sum = 0
    for i in new_lst:
        sum += i
    return sum

print('Dot MyName   and   MyName = ', dot_product(dic['MyName'], dic['MyName']))
print('Dot YourName and YourName = ', dot_product(dic['YourName'], dic['YourName']))
print('Dot ThisName and ThisName = ', dot_product(dic['ThisName'], dic['ThisName']))
print('Dot ThatName and ThatName = ', dot_product(dic['ThatName'], dic['ThatName']))
print('testing dot with oneVector')
print('Dot MyName   and oneVector = ', dot_product(dic['MyName'], oneVector))
print('Dot YourName and oneVector = ', dot_product(dic['YourName'], oneVector))
print('Dot ThisName and oneVector = ', dot_product(dic['ThisName'], oneVector))
print('Dot ThatName and oneVector = ', dot_product(dic['ThatName'], oneVector))
print('\n')

print("===============")
print('Problem 4: Analyze vectors')
def dot_count(d, ele):
    x = dot_product(d, d)
    y = dot_product(d, oneVector)
    if ele == 1:
        z = (x - y)/2 + y
        return int(z)
    elif ele == -1:
        z = x - ((x - y)/2 + y)
        return int(z)
    else:
        z = len(d) - x
        return int(z)

print('MyName   : Number of 1:', dot_count(dic['MyName'], 1), 'number of -1:', dot_count(dic['MyName'], -1), 'number of zero:', dot_count(dic['MyName'], 0))
print('YourName : Number of 1:', dot_count(dic['YourName'], 1), 'number of -1:', dot_count(dic['YourName'], -1), 'number of zero:', dot_count(dic['YourName'], 0))
print('ThisName : Number of 1:', dot_count(dic['ThisName'], 1), 'number of -1:', dot_count(dic['ThisName'], -1), 'number of zero:', dot_count(dic['ThisName'], 0))
print('ThatName : Number of 1:', dot_count(dic['ThatName'], 1), 'number of -1:', dot_count(dic['ThatName'], -1), 'number of zero:', dot_count(dic['ThatName'], 0))

    
    
