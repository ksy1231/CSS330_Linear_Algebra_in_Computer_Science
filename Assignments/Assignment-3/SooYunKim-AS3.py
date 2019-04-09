f = open("voting_record_dump109.txt")
list = list(f)
dict = dict()
d = {}
al = []
for l in list:
    al = l.split()
    dict[al[0]] = [int(al[v]) for v in range(3, len(al))]
    d[al[0]] = " ".join(al[1:2])

oneVector = [1 for v in range(46)]

def dot_product(v1, v2):
    return sum([a*b for (a, b) in zip(v1, v2)])

def analyze_vector(name):
    v = dict[name]
    yesPlusNo = dot_product(v, v)
    yesMinusNo = dot_product(v, oneVector)
    yesTwice = yesPlusNo + yesMinusNo
    yesCount = yesTwice // 2
    noCount = yesPlusNo - yesCount
    abstainCount = len(v) - yesPlusNo
    print(f'{name:11} : {d[name]:1}  Yes: {yesCount:2}  No: {noCount:2}  Absent: {abstainCount:1}')

def most_similar(name):
    max = 0
    str = ''
    for key in dict:
        if dict[name] == dict[key]:
            continue
        v = dot_product(dict[name], dict[key])
        if v > max:
            max = v
            str = key
        elif v == max:
            max = v
            str += ' ' + key
    l = []
    l = str.split()
    print('               Most similar: Policy similarity=', max)
    print(f'               Most similar senator set (size={len(l):1}):', str)

def least_similar(name):
    min = 50
    str = ''
    for key in dict:
        if dict[name] == dict[key]:
            continue
        v = dot_product(dict[name], dict[key])
        if v < min:
            min = v
            str = key
        elif v == min:
            min = v
            str += ' ' + key
    l = []
    l = str.split()
    print('               Most similar: Policy similarity=', min)
    print(f'               Most similar senator set (size={len(l):1}):', str)

print("=====================================================================")
print("(A): Testing Task 2.12.1: The senator voting dictionary:")
print(dict)
print("=====================================================================")

print()
print("=====================================================================")
print("(B): Dumping all senator voting records (Total votes= 46)")
for key in dict:
    analyze_vector(f"{key}")
print("=====================================================================")

print()
print("=====================================================================")
print("(C): Testing Task 2.12.2 Compare Policies: Total votes= 46")
analyze_vector('Obama')
print('Obama and Biden      :', dot_product(dict['Obama'], dict['Biden']))
print('Obama and McCain     :', dot_product(dict['Obama'], dict['McCain']))
print('Obama and Bunning(KY):', dot_product(dict['Obama'], dict['Bunning']))
print('Obama and Cantwell   :', dot_product(dict['Obama'], dict['Cantwell']))
print('Obama and Murray     :', dot_product(dict['Obama'], dict['Murray']))
print()
analyze_vector('Shelby')
print('Shelby and Biden      :', dot_product(dict['Shelby'], dict['Biden']))
print('Shelby and McCain     :', dot_product(dict['Shelby'], dict['McCain']))
print('Shelby and Bunning(KY):', dot_product(dict['Shelby'], dict['Bunning']))
print('Shelby and Cantwell   :', dot_product(dict['Shelby'], dict['Cantwell']))
print('Shelby and Murray     :', dot_product(dict['Shelby'], dict['Murray']))
print()
analyze_vector('Mikulski')
print('Mikulski and Biden      :', dot_product(dict['Mikulski'], dict['Biden']))
print('Mikulski and McCain     :', dot_product(dict['Mikulski'], dict['McCain']))
print('Mikulski and Bunning(KY):', dot_product(dict['Mikulski'], dict['Bunning']))
print('Mikulski and Cantwell   :', dot_product(dict['Mikulski'], dict['Cantwell']))
print('Mikulski and Murray     :', dot_product(dict['Mikulski'], dict['Murray']))
print("=====================================================================")

print()
print("=====================================================================")
print("(D): Testing Task 2.12.3 Most simliar set: Total votes= 46")
analyze_vector('Obama')
most_similar('Obama')
print()
analyze_vector('McCain')
most_similar('McCain')
print()
analyze_vector('Lincoln')
most_similar('Lincoln')
print()
analyze_vector('Santorum')
most_similar('Santorum')
print()
analyze_vector('Cantwell')
most_similar('Cantwell')
print()
analyze_vector('Murray')
most_similar('Murray')
print("=====================================================================")

print()
print("=====================================================================")
print("(E): Testing Task 2.12.4 Least simliar set: Total votes= 46")
analyze_vector('Obama')
least_similar('Obama')
print()
analyze_vector('McCain')
least_similar('McCain')
print()
analyze_vector('Lincoln')
least_similar('Lincoln')
print()
analyze_vector('Santorum')
least_similar('Santorum')
print()
analyze_vector('Cantwell')
least_similar('Cantwell')
print()
analyze_vector('Murray')
least_similar('Murray')
print("=====================================================================")
